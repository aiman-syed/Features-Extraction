import nltk


def percentageOfCapitalLetters(text):

   count= 0
   no_of_chars=0
   
   ##splitting in words##
   words = nltk.word_tokenize(text)

    
   ###caluculating no of chars###
   for word in words:
      no_of_chars+=len(word)
      l=list(word)
      ###calculating capital letters###
      for c in l:
         if c.isupper():
               count+=1

   return float(count*100)/no_of_chars