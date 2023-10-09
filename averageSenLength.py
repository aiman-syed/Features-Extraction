import nltk
from nltk.tokenize import RegexpTokenizer

def averageSenLength(text):
  
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)
   #print sentences
   #print no_of_sen

   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)
   #print words
   #print no_of_words

   return no_of_words/no_of_sen