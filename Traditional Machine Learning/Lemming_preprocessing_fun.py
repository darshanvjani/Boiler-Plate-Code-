
'''
Function 
1) Convert Sentence into Lower
2) Word Tokenize it
3) Remove Punctuations
4) Remove stop_words
5) Remove words with number (regex)
6) Lemmatization of words
7) Joining the tokens into one sentense.
'''

def lemma_fun(x):
  x = str(x).lower()
  sentence_words = nltk.word_tokenize(x)
  for word in sentence_words:
    if word in punctuations:
      sentence_words.remove(word)
    elif word in stop_words:
      sentence_words.remove(word)
    elif re.search(r'(\d)+',word):
      sentence_words.remove(word)
  sentense_list = []
  for word in sentence_words:
    sentense_list.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
  return ' '.join(x for x in sentense_list)


