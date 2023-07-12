# Import libraries
import string
import re
from numpy import array, argmax, random, take
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding, RepeatVector
from keras.preprocessing.text import Tokenizer
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras import optimizers
import matplotlib.pyplot as plt

#%matplotlib inline
pd.set_option('display.max_colwidth', 200)

# Function to read raw text file
def read_text(filename):
    # open the file
    file = open(filename, mode='rt', encoding='utf-8')

    # read all text
    text = file.read()
    file.close()
    return text

# Split a text into sentences
def to_lines(text):
    sents = text.strip().split('\n')
    sents = [i.split('\t') for i in sents]
    return sents

# Load dataset
data = read_text("data/bilingual-sentence-pairs/deu.txt")
deu_eng = to_lines(data)
deu_eng = array(deu_eng)
## We will use only the first 50,000 sentence pairs to reduce the training time of the model
deu_eng = deu_eng[:50000,:]

# Remove punctuation
deu_eng[:,0] = [s.translate(str.maketrans('', '', string.punctuation)) for s in deu_eng[:,0]]
deu_eng[:,1] = [s.translate(str.maketrans('', '', string.punctuation)) for s in deu_eng[:,1]]

deu_eng

# Convert text to lowercase
for i in range(len(deu_eng)):
    deu_eng[i,0] = deu_eng[i,0].lower()
    deu_eng[i,1] = deu_eng[i,1].lower()

# Empty lists
eng_l = []
deu_l = []

# Populate the lists with sentence lengths
for i in deu_eng[:,0]:
    eng_l.append(len(i.split()))

for i in deu_eng[:,1]:
    deu_l.append(len(i.split()))
## Plot the distributions
import pylab as pl
length_df = pd.DataFrame({'eng':eng_l, 'deu':deu_l})
length_df.hist(bins = 30)
pl.suptitle("Distributions of sentence lengths (eng vs deu)")
plt.show()
## Find the max sentence length for each language
max_eng_sentence_length = max(length_df['eng'])
max_deu_sentence_length = max(length_df['deu'])
print('Max sentence length for eng: %d' % max_eng_sentence_length)
print('Max sentence length for deu: %d' % max_deu_sentence_length)

# Function to build a tokenizer
def tokenization(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer

# Prepare english tokenizer
eng_tokenizer = tokenization(deu_eng[:, 0])
eng_vocab_size = len(eng_tokenizer.word_index) + 1
## Choose "7" as the max sentence length
eng_length = 7
print('English Vocabulary Size: %d' % eng_vocab_size)

# Prepare Deutch tokenizer
deu_tokenizer = tokenization(deu_eng[:, 1])
deu_vocab_size = len(deu_tokenizer.word_index) + 1
## Choose "7" as the max sentence length
deu_length = 7
print('Deutch Vocabulary Size: %d' % deu_vocab_size)

# Encode and pad sequences
def encode_sequences(tokenizer, length, lines):
    seq = tokenizer.texts_to_sequences(lines)
    ## Pad sequences with 0 values
    seq = pad_sequences(seq, maxlen=length, padding='post')
    return seq

# Model building
from sklearn.model_selection import train_test_split
## Split data into train and test set
train, test = train_test_split(deu_eng, test_size=0.2, random_state = 12)

# Prepare training data
trainX = encode_sequences(deu_tokenizer, deu_length, train[:, 1])
trainY = encode_sequences(eng_tokenizer, eng_length, train[:, 0])

# Prepare validation data
testX = encode_sequences(deu_tokenizer, deu_length, test[:, 1])
testY = encode_sequences(eng_tokenizer, eng_length, test[:, 0])

# Define the model
## Build NMT model
def define_model(in_vocab,out_vocab, in_timesteps,out_timesteps,units):
    model = Sequential()
    model.add(Embedding(in_vocab, units, input_length=in_timesteps, mask_zero=True))
    model.add(LSTM(units))
    model.add(RepeatVector(out_timesteps))
    model.add(LSTM(units, return_sequences=True))
    model.add(Dense(out_vocab, activation='softmax'))
    return model
## Model compilation
model = define_model(deu_vocab_size, eng_vocab_size, deu_length, eng_length, 512)
rms = optimizers.RMSprop(lr=0.001)
model.compile(optimizer=rms, loss='sparse_categorical_crossentropy')

# Fit the model
## Save the model with the lowest validation loss
filename = 'model.h1.28_may_23'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

# Train model
history = model.fit(trainX, trainY.reshape(trainY.shape[0], trainY.shape[1], 1),
                    epochs=30, batch_size=512, validation_split = 0.2,callbacks=[checkpoint],
                    verbose=1)
## Plot validation loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['train','validation'])
plt.show()

# Prediction on unseen data
from keras.models import load_model
model = load_model('model.h1.28_may_23')
preds = model.predict_classes(testX.reshape((testX.shape[0],testX.shape[1])))

# Present the results in dataframe (eng)
def get_word(n, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == n:
            return word
    return None

preds_text_eng = []
for i in preds:
    temp = []
    for j in range(len(i)):
        t = get_word(i[j], eng_tokenizer)
        if j > 0:
            if (t == get_word(i[j-1], eng_tokenizer)) or (t == None):
                temp.append('')
            else:
                temp.append(t)
        else:
            if(t == None):
                temp.append('')
            else:
                temp.append(t)

    preds_text_eng.append(' '.join(temp))

pred_df_eng = pd.DataFrame({'actual' : test[:,0], 'predicted' : preds_text_eng})
## Print 15 rows randomly
print(pred_df_eng.head(15))

# Present the results in dataframe (deu)
def get_word(n, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == n:
            return word
    return None

preds_text_deu = []
for i in preds:
    temp = []
    for j in range(len(i)):
        t = get_word(i[j], deu_tokenizer)
        if j > 0:
            if (t == get_word(i[j-1], deu_tokenizer)) or (t == None):
                temp.append('')
            else:
                temp.append(t)
        else:
            if(t == None):
                temp.append('')
            else:
                temp.append(t)

    preds_text_deu.append(' '.join(temp))

pred_df_deu = pd.DataFrame({'actual' : test[:,1], 'predicted' : preds_text_deu})
## Print 15 rows randomly
print(pred_df_deu.head(15))
