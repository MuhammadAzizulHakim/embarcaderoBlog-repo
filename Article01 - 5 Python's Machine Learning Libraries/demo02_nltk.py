from nltk.corpus import treebank

# Display a parse tree from corpus treebank
t = treebank.parsed_sents('wsj_0009.mrg')[0]
t.draw() # opens a new window.