# import statements
import numpy as np
import pandas as pd
import string
from collections import Counter
# Import linear_kernel
from sklearn.metrics.pairwise import linear_kernel
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
import json

#####################################################
################ USER INPUT OPTIONS #################
#####################################################

city = 'Las Vegas'
# A list containing the buisness ID of all the users favorite restaurants
user_fav_restaurants = ['ngs16C2M_uTq2zXamltHVw']


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
############### FUNCTIONS FOR ALGORITHM #############
#####################################################

# Function that takes in a list of restaurants as input and outputs most similar restaurants
def get_recommendations(title, cosine_sim, restDF):
    sim_scores = [(0, 0)]*cosine_sim.shape[0]
    for t in title:
      # Get the index of the restaurant that matches the title
      print("evaluating restaurant", t)
      idx = indices[t]
      print("scoring")
      # Get the pairwsie similarity scores of all restaurants with that restaurant
      scores = list(enumerate(cosine_sim[idx]))
      print("aggregating scores")
      sim_scores = [(i, scores[i][1] + sim_scores[i][1]) for i in range(cosine_sim.shape[0])]
    # Sort the restaurants based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar restaurants
    sim_scores = sim_scores[1:11]
    
    # Get the restaurants indices
    print("retrieving indices")
    movie_indices = [i[0] for i in sim_scores]
    print("returning value")
    # Return the top 10 most similar restauratns
    return restDF['business_id'].iloc[movie_indices]
  
# function that converts the ids to names
def idToName(recs):
  alist = []
  for i in recs:
    print(str(restaurants[i]["stars"]) + " " + restaurants[i]["name"])
    alist.append([(restaurants[i]["stars"]), restaurants[i]["name"]])
  return alist


#####################################################
#################### NEEDED FILES ###################
#####################################################

df_attr = loadData("cleanedRestaurantAttributes.csv")

import json
def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

restaurants = js_r('restaurantAttrDict.json')


#####################################################
################ RUNNING ALGORITHM ##################
#####################################################

# filtering down to city
filtered = df_attr[df_attr.city == city]
filtered.reset_index(drop=True, inplace=True)


# droping columns: name, address, city, business_id
filtered2 = filtered.drop('name', axis=1)
filtered2 = filtered2.drop('address', axis = 1)
filtered2 = filtered2.drop('city', axis=1)
filtered2 = filtered2.drop('business_id', axis=1)

# converting pandas dataframe to np_array
filtered2 = filtered2.values

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(filtered2, filtered2)

# Construct a reverse map of indices and restaurant titles
# filtered.reset_index(drop=True, inplace=True)
indices = pd.Series(filtered.index, index=filtered['business_id']).drop_duplicates()

# Generate Recommendations 
recs = get_recommendations(user_fav_restaurants, cosine_sim, filtered)
recs = idToName(recs)
print(recs)