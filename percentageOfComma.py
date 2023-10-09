import nltk


def percentageOfComma(text):

   count= 0
   no_of_chars=0
   
   #splitting in words
   words = nltk.word_tokenize(text)

    
   #caluculating no of chars
   
   for word in words:
      no_of_chars+=len(word)

  
   count=words.count(',')
    
   
   return float(count*100)/no_of_chars