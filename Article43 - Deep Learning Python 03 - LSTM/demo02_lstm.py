# Import libraries
import os
import sys
from keras.models import Model
from keras.layers import Input, LSTM, GRU, Dense, Embedding
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
from numpy import array # For loading GloVe data
from numpy import asarray # For loading GloVe data
from numpy import zeros # For loading GloVe data
from keras.utils import plot_model # For plotting DL models

# Set values for different parameters
BATCH_SIZE = 64
EPOCHS = 30
LSTM_NODES = 256
NUM_SENTENCES = 20000
MAX_SENTENCE_LENGTH = 50
MAX_NUM_WORDS = 20000
EMBEDDING_SIZE = 100

# Data preprocessing
input_sentences = []
output_sentences = []
output_sentences_inputs = []

count = 0
for line in open("data/bilingual-sentence-pairs/deu.txt", encoding="utf-8"):
    count += 1

    if count > NUM_SENTENCES:
        break

    if '\t' not in line:
        continue

    input_sentence, output, _ = line.rstrip().split('\t')

    output_sentence = output + ' <eos>'
    output_sentence_input = '<sos> ' + output

    input_sentences.append(input_sentence)
    output_sentences.append(output_sentence)
    output_sentences_inputs.append(output_sentence_input)

print("num samples input:", len(input_sentences))
print("num samples output:", len(output_sentences))
print("num samples output input:", len(output_sentences_inputs))

# Randomly print sentences
print(input_sentences[172])
print(output_sentences[172])
print(output_sentences_inputs[172])

# Tokenization (for inputs)
input_tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
input_tokenizer.fit_on_texts(input_sentences)
input_integer_seq = input_tokenizer.texts_to_sequences(input_sentences)

word2idx_inputs = input_tokenizer.word_index
print('Total unique words in the input: %s' % len(word2idx_inputs))

max_input_len = max(len(sen) for sen in input_integer_seq)
print("Length of longest sentence in input: %g" % max_input_len)

# Tokenization (for outputs)
output_tokenizer = Tokenizer(num_words=MAX_NUM_WORDS, filters='')
output_tokenizer.fit_on_texts(output_sentences + output_sentences_inputs)
output_integer_seq = output_tokenizer.texts_to_sequences(output_sentences)
output_input_integer_seq = output_tokenizer.texts_to_sequences(output_sentences_inputs)

word2idx_outputs = output_tokenizer.word_index
print('Total unique words in the output: %s' % len(word2idx_outputs))

num_words_output = len(word2idx_outputs) + 1
max_out_len = max(len(sen) for sen in output_integer_seq)
print("Length of longest sentence in the output: %g" % max_out_len)

# Padding
encoder_input_sequences = pad_sequences(input_integer_seq, maxlen=max_input_len)
print("encoder_input_sequences.shape:", encoder_input_sequences.shape)
print("encoder_input_sequences[172]:", encoder_input_sequences[172])
## Verify the integer values for "go" and "away" (sentence index 172)
print(word2idx_inputs["go"])
print(word2idx_inputs["away"])
## In the same way, padd the decoder outputs and the decoder inputs (deu):
decoder_input_sequences = pad_sequences(output_input_integer_seq, maxlen=max_out_len, padding='post')
print("decoder_input_sequences.shape:", decoder_input_sequences.shape)
print("decoder_input_sequences[172]:", decoder_input_sequences[172])
### Print the corresponding integers from the word2idx_outputs (sentence index 172)
print(word2idx_outputs["<sos>"])
print(word2idx_outputs["mach"])
print(word2idx_outputs["’ne"])
print(word2idx_outputs["fliege!"])

# Create word embeddings for the inputs by load the GloVe word vectors into memory
embeddings_dictionary = dict()

glove_file = open("data/glove/glove.6B.100d.txt", encoding="utf-8")
for line in glove_file:
    records = line.split()
    word = records[0]
    vector_dimensions = asarray(records[1:], dtype='float32')
    embeddings_dictionary[word] = vector_dimensions
glove_file.close()

## Create a matrix where the row number will represent the integer value for the word and the columns will correspond to the dimensions of the word
num_words = min(MAX_NUM_WORDS, len(word2idx_inputs) + 1)
embedding_matrix = zeros((num_words, EMBEDDING_SIZE))
for word, index in word2idx_inputs.items():
    embedding_vector = embeddings_dictionary.get(word)
    if embedding_vector is not None:
        embedding_matrix[index] = embedding_vector
## Print the word embeddings for the word "go" using the GloVe word embedding dictionary.
print(embeddings_dictionary["go"])
print(embedding_matrix[20])
## Creates the embedding layer for the input
embedding_layer = Embedding(num_words, EMBEDDING_SIZE, weights=[embedding_matrix], input_length=max_input_len)

# Create the model
## The final shape of the output: (number of inputs, length of the output sentence, the number of words in the output)
## Creates the empty output array:
decoder_output_sequences = []  # Define decoder_output_sequences variable

for seq in output_integer_seq:
    decoder_output_sequences.append(seq[1:])  # Remove the first element "<sos>"

decoder_targets_one_hot = np.zeros((
        len(input_sentences),
        max_out_len,
        num_words_output
    ),
    dtype='float32'
)
## Prints the shape of the decoder:
print(decoder_targets_one_hot.shape)
## To make predictions, the final layer of the model will be a dense layer, therefore we need the outputs in the form of one-hot encoded vectors.
for i, d in enumerate(decoder_output_sequences):
    for t, word in enumerate(d):
        decoder_targets_one_hot[i, t, word] = 1
## Create the encoder for LSTM:
encoder_inputs_placeholder = Input(shape=(max_input_len,))
x = embedding_layer(encoder_inputs_placeholder)
encoder = LSTM(LSTM_NODES, return_state=True)

encoder_outputs, h, c = encoder(x)
encoder_states = [h, c]
## Create the decoder for LSTM:
decoder_inputs_placeholder = Input(shape=(max_out_len,))

decoder_embedding = Embedding(num_words_output, LSTM_NODES)
decoder_inputs_x = decoder_embedding(decoder_inputs_placeholder)

decoder_lstm = LSTM(LSTM_NODES, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs_x, initial_state=encoder_states)
## Pass the output from the decoder LSTM through a dense layer, to predict decoder outputs
decoder_dense = Dense(num_words_output, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Compile the model
model = Model([encoder_inputs_placeholder,
               decoder_inputs_placeholder], decoder_outputs)
model.compile(
    optimizer='rmsprop',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
## Plot our model
plot_model(model, to_file='plot_LSTMModelForMachineTranslation.png', show_shapes=True, show_layer_names=True)

# Train the model using the fit() method:
r = model.fit(
    [encoder_input_sequences, decoder_input_sequences],
    decoder_targets_one_hot,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_split=0.1,
)

# Modifying the model for predictions
## The encoder model remains the same:
encoder_model = Model(encoder_inputs_placeholder, encoder_states)
## Modify our model to accept the hidden and cell states
decoder_state_input_h = Input(shape=(LSTM_NODES,))
decoder_state_input_c = Input(shape=(LSTM_NODES,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
## At each time step, there will be only single word in the decoder input, we need to modify the decoder embedding layer as follows:
decoder_inputs_single = Input(shape=(1,))
decoder_inputs_single_x = decoder_embedding(decoder_inputs_single)
## Create the placeholder for decoder outputs:
decoder_outputs, h, c = decoder_lstm(decoder_inputs_single_x, initial_state=decoder_states_inputs)
## To make predictions, the decoder output is passed through the dense layer:
decoder_states = [h, c]
decoder_outputs = decoder_dense(decoder_outputs)
## The final step is to define the updated decoder model, as shown here:
decoder_model = Model(
    [decoder_inputs_single] + decoder_states_inputs,
    [decoder_outputs] + decoder_states
)
## Plot our modified decoder LSTM that makes predictions:
plot_model(decoder_model, to_file='plot_modifiedLSTMModelForMachineTranslation.png', show_shapes=True, show_layer_names=True)

# Making predictions
## Create new dictionaries for both inputs and outputs where the keys will be the integers and the corresponding values will be the words:
idx2word_input = {v:k for k, v in word2idx_inputs.items()}
idx2word_target = {v:k for k, v in word2idx_outputs.items()}

## Create translate_sentence() method to accept an input-padded sequence English sentence (in the integer form) and will return the translated French sentence.
def translate_sentence(input_seq):
    states_value = encoder_model.predict(input_seq)
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = word2idx_outputs['<sos>']
    eos = word2idx_outputs['<eos>']
    output_sentence = []

    for _ in range(max_out_len):
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
        idx = np.argmax(output_tokens[0, 0, :])

        if eos == idx:
            break

        word = ''

        if idx > 0:
            word = idx2word_target[idx]
            output_sentence.append(word)

        target_seq[0, 0] = idx
        states_value = [h, c]

    return ' '.join(output_sentence)

# Testing the model
i = np.random.choice(len(input_sentences))
input_seq = encoder_input_sequences[i:i+1]
translation = translate_sentence(input_seq)
print('-')
print('Input:', input_sentences[i])
print('Response:', translation)
