from flask import Flask
from flask import request, jsonify
from flask import render_template, render_template_string


import json

app = Flask(__name__)
app.config["DEBUG"] = True

with open("./data/recommendDict.json", "r") as a:
    recommendations = json.load(a)
with open("./data/associationRuleDict.json", "r") as b:
    associationRules = json.load(b)
with open("./data/wordToStemDict.json", "r") as c:
    wordToStem = json.load(c)
with open("./data/restaurantAttrDict.json", "r") as d:
    restaurantAttributes = json.load(d)

# APP/HOME
@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html')

# APP/API/
@app.route('/api', methods=['GET'])
def apiHome():
    return "<h1>Restaurant API</h1><p>test me bud</p>"

# RESTAURANT ATTRIBUTES
@app.route('/api/resources/restaurants/attributes/all', methods=['GET'])
def returnAllRestaurantAttributes():
    return jsonify(restaurantAttributes)

@app.route('/api/resources/restaurants/attributes/', methods=['GET'])
def returnRestaurantAttributesID():
    try:
        if 'id' in request.args:
            id = str(request.args['id'])
        else:
            return "no id specified (format url as ../attributes?id=RESTAURANT_ID to get a result)"
        return restaurantAttributes[id]
    except KeyError:
        return "could not find restaurant"

# WORD STEMS
@app.route('/api/resources/stems/all', methods = ['GET'])
def returnAllStems():
    return jsonify(wordToStem)

@app.route('/api/resources/stems/', methods = ['GET'])
def returnStem():
    try:
        if 'word' in request.args:
            word = str(request.args['word'])
        else:
            return "no word specified (format url as ../stems?word=YOUR_WORD to get a result)"
        return wordToStem[word]

    except KeyError:
       return "no stem found"

# ASSOCIATION RULES
@app.route('/api/resources/associationRules/all', methods=['GET'])
def returnAllRules():
    return jsonify(associationRules)

@app.route('/api/resources/associationRules/', methods=['GET'])
def returnRulesByWord():
    try:
        if 'word' in request.args:
            word = str(request.args['word'])
        else:
            return "specify word"
        return associationRules[word]

    except KeyError:
        return "word not found"

# RECOMMENDATIONS
@app.route('/api/resources/recommendations/all')
def returnAllRecommendations():
    return jsonfiy(recommendations)

@app.route('/api/resources/recommendations/')
def returnRecommendationsID():
    try:
        if 'id' in request.args:
            id = str(request.args['id'])
        else:
            return "no id specified"
        return recommendations[id]

    except KeyError:
        return "no recommendations found"
