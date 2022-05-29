import pickle
import os
import pandas as pd
import requests
from core.constants import Debug
# from PIL import Image


# from pathlib import Path
# patha = Path(__file__).parent / "../datasets/dataframe.pkl"
# pathb = Path(__file__).parent / "../datasets/similarityBert.pkl"
# print(patha)

my_path = os.path.abspath(os.path.dirname(__file__))
patha = os.path.join(my_path, "../datasets/dataframe1.pkl")
pathb = os.path.join(my_path, "../datasets/similarityBert.pkl")
if Debug:
    print(patha)
    print(pathb)

dataframe = pickle.load(open(patha, 'rb'))
dataframe = dataframe.to_dict()
movies_df = pd.DataFrame(dataframe)
similarityBert = pickle.load(open(pathb, 'rb'))

if Debug:
    print(111)
def Recommend(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarityBert[index])), reverse=True, key = lambda x: x[1])
    if Debug:
        print("before loop")
    movie_recommendation = []
    for i in distances[1:20]:
        movie_recommendation.append(movies_df.iloc[i[0]].movie_id)
        if Debug:
            print(movies_df.iloc[i[0]].title)
            print(movies_df.iloc[i[0]].movie_id)

    return movie_recommendation


if Debug:
    Recommend('Harry Potter and the Philosopher\'s Stone')
    Recommend('The Avengers')


path_poster = os.path.join(my_path, "../static/unavailable.jpg")
if Debug:
    print(path_poster)

def Fetch_poster(movie_id):
    try:
        response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c8d2cdd82e972178b58d5fd8cb4295b1&language=en-US'.format(movie_id))
    except requests.ConnectionError:
        response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c8d2cdd82e972178b58d5fd8cb4295b1&language=en-US'.format(movie_id))
        return "https://upload.wikimedia.org/wikipedia/commons/a/ad/BolexH16.jpg"
    data= response.json()
    # if type(data['poster_path']) == 'str':
    #     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    # else:
    #     return "Poster Unavailable"
    try:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except KeyError:
        return "https://upload.wikimedia.org/wikipedia/commons/a/ad/BolexH16.jpg"
    except TypeError:
        return  "https://upload.wikimedia.org/wikipedia/commons/a/ad/BolexH16.jpg"

if Debug:
    poster = Fetch_poster(62)
    print(poster)
    # img = Image.open(r"{}".format(poster))
    # img.show()


