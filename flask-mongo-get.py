from flask import Flask, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'MyDb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/MyDb'

mongo = PyMongo(app)

#return all sorted by popularity

@app.route('/MyCollection', methods=['GET'])
def get_all_MyCollection():
    MyCollection = mongo.db.MyCollection
    res=[]
    for i in MyCollection.find():
        res.append({"Name":i['Name'],"Rating(Imdb)":i['Rating(Imdb)'],"Cast":i['Cast']})
    return jsonify({'movie': res})


#prefix


@app.route('/MyCollection/', methods=['GET'])
def get_all_MyCollection(name):
    MyCollection = mongo.db.MyCollection
    res=[]
    for i in MyCollection.find():
        if(i['Name'].startswith(name))
        res.append({"Name":i['Name'],"Rating(Imdb)":i['Rating(Imdb)'],"Cast":i['Cast']})
    return jsonify({'movie': res})

if __name__ == '__main__':
    app.run(debug=True)
