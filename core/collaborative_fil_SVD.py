import os
import pickle

import pandas as pd
from collections import defaultdict

from core.constants import Debug
Debug = 0

my_path = os.path.abspath(os.path.dirname(__file__))
path_pred = os.path.join(my_path, "../datasets/predictions.pkl")
path_data = os.path.join(my_path, "../datasets/data_cf.pkl")
path_data_obj = os.path.join(my_path, "../datasets/dataframe_obj.pkl")
if Debug:
    print(path_pred)
    print(path_data)
    print(path_data_obj)

prediction_matrix = pickle.load(open(path_pred, 'rb'))
data_cf = pickle.load(open(path_data, 'rb'))
dataframe_obj = pickle.load(open(path_data_obj, 'rb'))

def Get_top_n(userId, predictions = prediction_matrix, movies_df = dataframe_obj, ratings_df = data_cf[['movie_id', 'userid', 'rating']], n=10):

 # Part I.:

 # 1. First map the predictions to each user.
 top_n = defaultdict(list)
 for uid, iid, true_r, est, _ in predictions:
     top_n[uid].append((iid, est))

 # 2. Then sort the predictions for each user and retrieve the k highest ones.
 for uid, user_ratings in top_n.items():
     user_ratings.sort(key=lambda x: x[1], reverse=True)
     top_n[uid] = user_ratings[: n]

 # Part II.:

 # 3. Tells how many movies the user has already rated
 user_data = ratings_df[ratings_df.userid == (userId)]
 print('User {0} has already rated {1} movies.'.format(userId, user_data.shape[0]))

 # 4. Data Frame with predictions.
 preds_df = pd.DataFrame([(id, pair[0], pair[1]) for id, row in top_n.items() for pair in row],
                         columns=["userId", "movie_id", "rat_pred"])
 print("part2.4 done")

 # 5. Return pred_usr, i.e. top N recommended movies with (merged) titles and genres.
 pred_usr = preds_df[preds_df["userId"] == (userId)].merge(movies_df, how='left', left_on='movie_id',
                                                           right_on='movie_id')
 # .astype(int)
 print("part2.5 done")
 # 6. Return hist_usr, i.e. top N historically rated movies with (merged) titles and genres for holistic evaluation
 hist_usr = ratings_df[ratings_df.userid == (userId)].sort_values("rating", ascending=False).merge \
     (movies_df, how='left', left_on='movie_id', right_on='movie_id')

 return hist_usr, pred_usr

if Debug:
 hist_SVD_124, pred_SVD_124 = Get_top_n(10)
 print(hist_SVD_124.head(5))
 print(pred_SVD_124.head(5))

