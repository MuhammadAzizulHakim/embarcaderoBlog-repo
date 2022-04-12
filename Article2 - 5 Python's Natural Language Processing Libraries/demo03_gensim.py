import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Creating the Corpus
from collections import defaultdict
from gensim import corpora

documents = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

# Remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [
    [word for word in document.lower().split() if word not in stoplist]
    for document in documents
]

# Remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [
    [token for token in text if frequency[token] > 1]
    for text in texts
]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Similarity interface
from gensim import models
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # Convert the query to LSI space
print(vec_lsi)

# We will be considering `cosine similarity <http://en.wikipedia.org/wiki/Cosine_similarity>`_
# to determine the similarity of two vectors.

# Initializing query structures
from gensim import similarities
index = similarities.MatrixSimilarity(lsi[corpus]) # Transform corpus to LSI space and index it

index.save('C:/Users/ASUS/deerwester.index')
index = similarities.MatrixSimilarity.load('C:/Users/ASUS/deerwester.index')

# Performing queries
sims = index[vec_lsi] # Perform a similarity query against the corpus
print(list(enumerate(sims))) # Print (document_number, document_similarity) 2-tuples

# Cosine measure returns similarities in the range `<-1, 1>` (the greater, the more similar),
# so that the first document has a score of 0.99809301 etc.

sims = sorted(enumerate(sims), key=lambda item: -item[1])
for doc_position, doc_score in sims:
    print(doc_score, documents[doc_position])