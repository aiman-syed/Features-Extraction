import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfLongSen(text):
   
   count=0
  
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)
   
   #print no_of_sen

   for sen in sentences:
     tokenizer = RegexpTokenizer(r'\w+')
     words = tokenizer.tokenize(text)
     if len(words) > 15:
        count+=1

   return (count*100)/no_of_sen
   
   no_of_words = len(words)