from requests import get
from bs4 import BeautifulSoup as bs
#url = 'https://www.imdb.com/search/title/?release_date=2016-01-01,2019-06-30&languages=hi&count=250'
#response = get(url)
#print(response.text[:500])

#htm = bs(response.text,'html.parser')
#print(type(htm))

#movie = htm.find_all('div', class_ = 'lister-item mode-advanced')

#print(type(movie))
#print(len(movie))
#print(movie[0])
#first_movie = movie[1]
#print(first_movie.a)
#print(first_movie.h3.a)
#first_name = first_movie.h3.a.text
#print(first_name)
#print(first_movie.strong.text)
#first_cast = first_movie.find('p', class_ = "").text.strip(',').replace('\n','')
#first_cast = first_cast.split('Stars:')
#print(first_cast[1])


#############################################################################

url_list = ['https://www.imdb.com/search/title/?release_date=2016-01-01,2019-06-30&languages=hi&count=250',
            'https://www.imdb.com/search/title/?release_date=2016-01-01,2019-06-30&languages=hi&count=250&start=251&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2016-01-01,2019-06-30&languages=hi&count=250&start=501&ref_=adv_nxt',
            'https://www.imdb.com/search/title/?release_date=2016-01-01,2019-06-30&languages=hi&count=250&start=751&ref_=adv_nxt']
name = []
rating = []
cast = []

for ur in url_list:
            respornse = get(ur)
            html = bs(response.text,'html.parser')
            movies = html.find_all('div', class_ = 'lister-item mode-advanced')
            for i in movies:
                name.append(i.h3.a.text)
                if(i.strong!=None):
                    rating.append(i.strong.text)
                else:
                    rating.append(0)
                j = i.find('p', class_ = "").text.strip(',').replace('\n','')
                j = j.split('Stars:')
                cast.append(j[1])
#print(name)
#print(cast)
#print(rating)

###############################################################################

import pandas as pd
df = pd.DataFrame({'Name': name,'Rating(Imdb)': rating,'Cast': cast})
print(df.info())
print(df)

###############################################################################

from pymongo import MongoClient
import json

client = MongoClient()
db = client['MyDb']
col = db['MyCollection']

#dict_df = df.to_dict(orient='list')

df_json = json.loads(df.to_json(orient='records'))
col.insert_many(df_json)
