import nltk
from nltk.tokenize import RegexpTokenizer

def percentageOfwords(text):
   
   count=0
  
   sentences = nltk.sent_tokenize(text)
   no_of_sen = len(sentences)
    
   #print sentences   

   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)
   
   #print no_of_words
   #print words
   
   
   for word in words:
       if (len(word) ==2 or len(word)==3):
          count+=1
   #print count

   return float(count*100)/no_of_words
   