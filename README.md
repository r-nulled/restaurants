<<<<<<< HEAD
# DVA
Fall 2019
=======
# CX4242_Project

_____________________________________________________________________________________________
_____________________________________________________________________________________________
_____________________________________________________________________________________________


# FinalDataProcessing.dbc

DESCRIPTION
-----------
Further pre-processing on databricks in order to:
	(1) find the most important words users use in their comments.
	(2) generate a dictionary mapping between stem words and words
	(3) generate a dictionary mapping between restaurants (and thier ratings) and stem words
		found in their comments

HOW TO RUN
----------
Simply run cells in databricks (this file is only used for pre-processing)

_____________________________________________________________________________________________
_____________________________________________________________________________________________
_____________________________________________________________________________________________

# LasVegasKeyWordRec.py and PittsburghKeyWordRec.py

DESCRIPTION
-----------
This script uses an apriori model to make use of user's restaurant comments. Using the 
apriori model, the script learns what key words are most closely related - for instance,
the words breakfast, bacon, and eggs are all deffined to be closely related.
 
In this model "closely related" means: user who use word x also tend to use word y.

HOW IT WORKS
------------
The user input will be a key word
The output of the script will be a list containing the reccomended key words.

Example) 
suppose we have

user_key_word = 'bread'

then we can get reccomend key words via the function call
note that key_word_reccomendations and any other needed files are loaded automatically when
running the script. These two lines of code are all that the person using the script needs
to implement

suggestedKeyWords(key_word_reccomendations, user_key_word)

HOW TO RUN
----------
To run, simply implement/modify the following line at the beginning of the script under the section
USER INPUT OPTIONS. Note 'bread' can be chaged to any valid key word.
The result will be stored in the variable "suggestions" at then of the file (and will be printed).

user_key_word = 'bread'

Las Vegas - Then run the following from the command line:
python LasVegasKeyWordRec.py
Pittsburgh - Then run the following from the command line:
python PittsburghKeyWordRec.py

USE IN APPLICATION
------------------
The goal is to make choices easier for the user. Not only will we help them choose their
restaurant, but we will also help them learn what kind of restaurant they are looking for.

When a user selects a key word from the list of keyword choices, a pop-up bubble will appear.
This pop-up bubble will give the user a selection of keywords the user that may also
interest the user.

ADDITIONAL NEEDED FILES
-----------------------
associationRuleDict.json

_____________________________________________________________________________________________
_____________________________________________________________________________________________
_____________________________________________________________________________________________

# LasVegasRestaurantRec.py and PittsburghRestaurantRec.py 

DESCRIPTION
-----------
This script uses a similarity function to generate restaurant recommendations based on the
user chosen key words and restaurant ratings.

HOW IT WORKS
------------
The user input will be a list of key words
The output of the script will be a list of lists containing the reccomended restaurants and their overall ratings.

Example) 
suppose we have 

user_key_words = [('chicken', 5), ('bread', 2.5), ('dessert', 4)]

then we can get reccomend restaurants via the function call below
note that wordToStemDict, recommendDict, and any other needed files are loaded automatically when
running the script. These four lines of code are all that the person using the script needs
to implement

num = 10
recommendations = recommendRestaurant(user_key_words, num, wordToStemDict, recommendDict)
recommendations = idToName(recommendations)

Example Output: [['4.0', 'Sur La Table'], ['5.0', 'Chef @ Your Home'], ['4.5', 'Walnut Wednesdays'], ['5.0', 'Express Deli '], ['4.5', "Arnold's Tea"]]

HOW TO RUN
----------
To run, simply implement/modify the following TWO lines at the beginning of the script under the section
USER INPUT OPTIONS. Note user_key_words and num can be chaged to any valid key words and integers respectively. 
The result will be stored in the varable recommendations at the end of the file (and will be printed)

user_key_words = [('chicken', 5), ('bread', 2.5), ('dessert', 4)]
num = 10	# number of recommended restaurants

Las Vegas - Then run the following from the command line:
python LasVegasRestaurantRec.py

Pittsburgh - Then run the following from the command line:
python PittsburghRestaurantRec.py

USE IN APPLICATION
------------------
This script reccomends restaurants based on key words.

After selecting their desired key words, restaurant recommendations will pop up on
the user end.

ADDITIONAL NEEDED FILES
-----------------------
restaurantAttrDict.json
wordToStemDict.json
recommendDict.json

_____________________________________________________________________________________________
_____________________________________________________________________________________________
_____________________________________________________________________________________________

# LasVegasAttributeBasedFiltering.py and PittsburghAttributeBasedFiltering.py

DESCRIPTION
-----------
This script uses a content based filteering methods to generate restaurant recommendations.
based on the user chosen favorite restaurants.

HOW IT WORKS
------------
The user input will be a list of restaurants.
The output of the script will be a list of lists containing the reccomended restaurants and their overall ratings.

Example) 
suppose we have 

city = 'Las Vegas'
user_fav_restaurants = ['ngs16C2M_uTq2zXamltHVw']

then we can get reccomend restaurants via the function call below
note that cosine_sim, filtered, and any other needed files are loaded automatically when
running the script. These four lines of code are all that the person using the script needs
to implement

recs = get_recommendations(user_fav_restaurants, cosine_sim, filtered)
recs = idToName(recs)

Example Output: [['4.0', 'Sur La Table'], ['5.0', 'Chef @ Your Home'], ['4.5', 'Walnut Wednesdays'], ['5.0', 'Express Deli '], ['4.5', "Arnold's Tea"]]

HOW TO RUN
----------
To run, simply implement/modify the following TWO lines at the BEGINNING of the script under the section
USER INPUT OPTIONS. 
Note city and user_fav_restaurants can be chaged to any valid key words.
The result will be saved in the variable recs (and printed) at the end of the file. 

city = 'Las Vegas'
user_fav_restaurants = ['ngs16C2M_uTq2zXamltHVw']

Las Vegas - Then run the following from the command line:
python LasVegasAttributeBasedFiltering.py

Pittsburgh - Then run the following from the command line:
python PittsburghAttributeBasedFiltering.py

USE IN APPLICATION
------------------
This script reccomends restaurants based on other restaurants the user likes.

After selecting other favoite restaurants, restaurant recommendations will pop up on
the user end.

ADDITIONAL NEEDED FILES
-----------------------
cleanedRestaurantAttributes.csv
restaurantAttrDict.json


_____________________________________________________________________________________________
_____________________________________________________________________________________________
_____________________________________________________________________________________________

# Apriori and Comments.dbc

DESCRIPTION
-----------

Contains further pre-processing to prepare data for Apriori model used in keyWordRec.py.
It will generate the associationRuleDict used in keyWordRec.py
This file also runs the apriori model similar to keyWordRec.py and generate restaurant
recommentations similar to RestaurantRec.py.

HOW TO RUN
----------
Simply run cells in databricks (this file is only used for pre-processing and running the
initial model)


_____________________________________________________________________________________________
_____________________________________________________________________________________________
_____________________________________________________________________________________________

Content Based Filtering.dbc

DESCRIPTION
-----------

Contains further pre-processing to prepare data for content based filtering.
Generates a cleaned csv file for faster model processing in attributeBasedFiltering.py

HOW TO RUN
----------
Simply run cells in databricks (this file is only used for pre-processing and running the
initial model)

>>>>>>> 6d2dd0217836e5c092397ffa4c301919f9ebfca2
