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
patha = os.path.join(my_path, "../datasets/dataframe.pkl")
pathb = os.path.join(my_path, "../datasets/similarity_bow.pkl")
if Debug:
    print(patha)
    print(pathb)

dataframe = pickle.load(open(patha, 'rb'))
dataframe = dataframe.to_dict()
movies_df = pd.DataFrame(dataframe)
similarity_bow = pickle.load(open(pathb, 'rb'))


def Recommend_bow(movie):
    index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity_bow[index])), reverse=True, key = lambda x: x[1])
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
    Recommend_bow('Stuart Little 2')
    Recommend_bow('Toy Story')
    Recommend_bow('Jurassic Park')
