import numpy as np
import pandas as pd
import string
from pandas import DataFrame


##############################################
################# SECTION 1 ##################
##############################################
### USING APRIORI TO LEARN MORE ABOUT USER ###
##############################################


#################################################################
##################### TOP WORDS AND STOP WORDS###################
#################################################################

# Top words 
topWords = ['food', 'service', 'chicken', 'menu', 'love', 'staff', 'friendly', 'pizza', 'sauce', 'fresh', 'cheese', 'wait', 'lunch', 'salad', 'bar', 'dinner', 'night', 'server', 'fries', 'small', 'vegas', 'hot', 'price', 'drinks', 'burger', 'rice', 'sandwich', 'fried', 'sushi', 'meat', 'breakfast', 'favorite', 'tasty', 'quality', 'soup', 'beef', 'atmosphere', 'drink', 'flavor', 'bread', 'spicy', 'pork', 'steak', 'waitress', 'beer', 'tacos', 'coffee', 'wine', 'buffet', 'family', 'fast', 'clean', 'dessert', 'actually', 'tables', 'disappointed', 'kind', 'half', 'maybe', 'decent', 'left', 'cream', 'husband', 'quick', 'waiter', 'bacon', 'chips', 'chinese', 'wings', 'mexican', 'wife', 'thai', 'tea', 'egg', 'eggs', 'bbq', 'crab', 'noodles', 'decor', 'group', 'party', 'patio', 'brunch', 'chocolate', 'crispy', 'burgers', 'cake', 'taco', 'seating', 'grilled', 'customers', 'music', 'care', 'serve', 'started', 'week', 'appetizer', 'beans', 'potatoes', 'variety', 'sandwiches', 'garlic', 'pasta', 'french', 'salsa', 'salmon', 'servers', 'kids', 'italian', 'seafood', 'burrito', 'potato', 'authentic', 'parking', 'saturday', 'tender', 'lobster', 'light', 'curry', 'ambiance', 'birthday', 'vegan', 'soft', 'onion', 'appetizers', 'sausage', 'dog', 'toast', 'vegetarian', 'crust', 'tomato', 'salty', 'pho', 'desserts', 'boyfriend', 'corn', 'onions', 'friday', 'salads', 'bartender', 'ribs', 'noodle', 'lamb', 'tuna', 'weekend', 'combo', 'cafe', 'reservation']

stop_words = ['i', 'im', 'ill', 'us', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", 'dont', '', 'didnt', 'got', 'went']


#####################################################
#### FUNCTION FOR LOADING BIG DATA AS TSV OR CSV ####
#####################################################

def loadData(file_location, delimiter = ","):
  file_type = "csv"

  # CSV options
  infer_schema = "false"
  first_row_is_header = "true"
#   delimiter = "\t"

  # The applied options are for CSV files. For other file types, these will be ignored.
  df = pd.read_csv(file_location, sep= delimiter)
  return df



#####################################
## FUNCTION TO GENERATE DATAFRAME ###
#####################################

def enumerateComments(df, topWords, a, b):
  text = [] 
  itt = a
  userDF = {} 
  for word in topWords:
    userDF[word] = []

  for index, row in df.iterrows():
    if itt == b:
      break
    itt += 1    
    txt = row['text']    
    if txt != None:
      stripped = splitAndRemovePunc(txt)
      stripped = removeStopWords(stripped)
      stripped = intersection(stripped, topWords)
      stm = stemWords(stripped)
      unique = set(stm)
    for word in topWords:
      if word in unique:
        #change this to word if needed for algorithm
        userDF[word].append(word)
      else:
        userDF[word].append('NaN')

  newDf = pd.DataFrame(userDF,columns= topWords)
  
  return newDf

#####################################
#### ASSOCIATED HELPER FUNCTIONS ####
#####################################

### FIND KEY WORDS ###
def splitAndRemovePunc(text):
  # split into words by white space
  words = text.split()

  # remove punctuation from each word
  words = [word.lower() for word in words]
  table = str.maketrans('', '', string.punctuation)
  stripped = [w.translate(table) for w in words]
  return stripped


### REMOVE DIGITS AND STOP WORDS ###
def removeStopWords(wordList):
  # remove stop words from text
  stripped = [w for w in wordList if not w in stop_words]
  # digits to ignore
  digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  #remove digits
  stripped = [w for w in stripped if not w in digits]
  return stripped


#### STEM WORDS ########
def stemWords(wordList):
  ps = PorterStemmer()

  stemmed = []
  for word in wordList:
      stemmed.append(ps.stem(word))
  return stemmed


#####################################################
######### FUNCTIONS FOR CREATING DICTIONARY #########
#####################################################

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
  

## CLASSIFY KEY WORDS IN ROWS a TO b ##
def classifyWords(df, topWords, a, b):
  business_id = []
  text = []
  stars = []
  stem = []
  
  itt = a
  for index, row in df.iterrows():
    if itt == b:
      break
    itt += 1
    bus = row['business_id']
    txt = row['text']
    strs = row['stars']
    if txt != None:
      stripped = splitAndRemovePunc(txt)
      stripped = removeStopWords(stripped)
      stripped = intersection(stripped, topWords)
      stm = stemWords(stripped)
      size = len(stripped)
      business_id += [bus]*size
      stars += [strs]*size
      text += stripped
      stem += stm
  newDf = {'business_id': business_id,
          'text': text,
          'stars': stars,
          'stem_word': stem}
  newDf = pd.DataFrame(newDf,columns= ['business_id', 'text', 'stem_word', 'stars'])
  return newDf


## send information from dataframe to dictionary ##
def toDict(df):
  adict = {}
  wordToStemDict = {}
  for index, row in df.iterrows():
    if row['text'] not in wordToStemDict:
      wordToStemDict[row['text']] = row['stem_word']
    if row['stem_word'] not in adict:
      adict[row['stem_word']] = {row['business_id']: [float(row['stars'])]}
    else:
      try:
        if row['business_id'] not in adict[row['stem_word']]:
          adict[row['stem_word']][row['business_id']] = [float(row['stars'])]
        else:
          adict[row['stem_word']][row['business_id']].append(float(row['stars']))
      except:
        print(row)
  return adict, wordToStemDict
  

#############################
## RECOMMEND KEY WORDS ######
#############################

import json
def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))



# print(key_word_reccomendations)
# Function returns other key words the user may be interested in

def suggestedKeyWords(adict, word):
  suggestions = []
  for i in range(len(adict[word])):
    suggestions.append(adict[word][i][1])
  return list(set(suggestions))

key_word_reccomendations = js_r('associationRuleDict.json')

# Example: what else aside of chicken?
print(suggestedKeyWords(key_word_reccomendations, 'bread'))


