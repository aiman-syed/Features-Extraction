import nltk
from nltk.tokenize import RegexpTokenizer
from textstat.textstat import textstat

file_name = input("Enter file name:")

# open file for reading
text = open("C:\\Users\\aiman\\Testing\\Testing\\author_id_001.txt", "r")

def averageSyllable(text):

   count = 0
   no_of_words =0
   
   tokenizer = RegexpTokenizer(r'\w+')
   words = tokenizer.tokenize(text)
   no_of_words = len(words)  

   
   for word in words:
       count+=textstat.syllable_count(word)
          
   
   return float(count)/no_of_words