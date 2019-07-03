import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["MyDb"]
mycol = mydb["MyCollection"]

res=[]
a = input()
for i in mycol.find():
  if(i['Name'].startswith(a)):
    res.append({"Name":i['Name'],"Rating(Imdb)":i['Rating(Imdb)'],"Cast":i['Cast']})

print(res)
