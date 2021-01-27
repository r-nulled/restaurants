##############################################
################# SECTION 2 ##################
##############################################
### USING USER KEY WORDS TO FIND RESTAURANT ##
##############################################

import numpy as np
import pandas as pd
import string
from pandas import DataFrame

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


#####################################################
############# FUNCTIONS FOR RECCOMENDING ############
#####################################################

## use user input to recommend a restaurant ##
def recommendRestaurant(user_input, num, wordToStemDict, adict):
  recs = {}
  for inp in user_input:
    stem = wordToStemDict[inp[0]]
    restaurants = adict[stem]
#     print(adict)
#     print(restaurants)
    for restaurant in restaurants:
      if restaurant not in recs:
        # restaurants[restaurant] is the list of all ratings for the given key word
        # ex) [2.0, 1.0, 4.0, 3.0]
        recs[restaurant] = (sum(restaurants[restaurant])/len(restaurants[restaurant]))*inp[1]
      else:
        recs[restaurant] += sum(restaurants[restaurant])/len(restaurants[restaurant])*inp[1]
  final = []
  for rec in recs:
    final.append((recs[rec], rec))
  final.sort(reverse= True)
  final = final[:num]
  return final

###########################################
############# HELPER FUNCTIONS ############
###########################################

# function that converts the ids to names
def idToName(recs):
	alist = []
	for i in recs:
		try:
			print(str(restaurants[i]["stars"]) + " " + restaurants[i]["name"])
			alist.append([(restaurants[i]["stars"]), restaurants[i]["name"]])
		except:
			pass
	return alist


# df_attr = loadData("dFile2.csv")
# print("Generating restaurant ID dictionary to save restaurant [name, address, city]")
# restaurants = {}
# for index, row in df_attr.iterrows():
#   restaurants[row['business_id']] = {'name': row['name'], 'address': row['address'], 'city': row['city'], 'stars': row['stars']}



import json
def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

restaurants = js_r('restaurantAttrDict.json')

#####################################################
############## SCRIPT FOR RECOMMENDING ##############
#####################################################

# User input
user_input = [('chicken', 5), ('bread', 2.5), ('dessert', 4)]
# How many restaurants to reccomend
num = 10

wordToStemDict = js_r('wordToStemDict.json')

recommendDict = js_r('recommendDict.json')

recommendations = recommendRestaurant(user_input, num, wordToStemDict, recommendDict)

temp = []
for i in recommendations:
  temp.append(i[1])

recommendations = idToName(temp)
print(recommendations)