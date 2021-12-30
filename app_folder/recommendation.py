

"""
contains various implementations for recommending movies
"""


import pandas as pd
import numpy as np
from utils import nmf_model, neighbor_model, movies, ratings, movie_to_id





# collaborative filtering = look at ratings only!
def recommend_nmf(query, k=10):
    
    """
    Filters and recommends the top k movies for any given input query based on a trained NMF model. 
    Returns a list of k movie ids.
    """
    # 1. candiate generation
    user_vec = np.repeat(0, 193610)
    user_vec[query] = 5
    # 2. scoring      
    # calculate the score with the NMF model
    scores = nmf_model.inverse_transform(nmf_model.transform([user_vec]))
    scores = pd.Series(scores[0])
    # 3. ranking
    # set zero score to movies allready seen by the user
    scores[query] = 0
    # return the top-k highst rated movie ids or titles
    scores = scores.sort_values(ascending = False)
    recommendations = scores.head(k).index
    return recommendations 


# collaborative filtering = look at ratings only!
def recommend_neighborhood(query, k=10):
    """
    Filters and recommends the top k movies for any given input query based on a trained nearest neighbors model. 
    Returns a list of k movie ids.
    """

    
    # 1. candiate generation
    # construct a user vector
    user_vec = np.repeat(0, 193610)
    user_vec[query] = 5
   
    # 2. scoring
    # find n neighbors
    distances, userIds = neighbor_model.kneighbors(
        X=[user_vec], 
        n_neighbors=5, 
        return_distance=True
    )
    neighborhood = ratings.loc[ratings['userId'].isin(userIds[0])]
    # calculate their average rating
    scores = neighborhood.groupby('movieId')['rating'].sum()
    
    # 3. ranking
    
    # filter out movies allready seen by the user
    # scores_query_to_zero = scores.index.isin(query)
    # scores.loc[scores_query_to_zero] = 0
    scores = scores.sort_values(ascending=False)
    # return the top-k highst rated movie ids or titles
    recommendations = scores.head(k).index
    return recommendations

def recommend_random(k=10):
    """
    Recommends a list of k random movie ids
    """
    recommendations = ratings['movieId'].sample(n=k)
    return recommendations

def recommend_popular():
    """
    Recommend a list of k movie ids that are the most popular
    """
    df = ratings.merge(movies, left_on='movieId', right_on='movieId', suffixes=(False, False))
    recommendations = (df['rating'].groupby(df['movieId']).count()).nlargest(10)
    recommendations = recommendations.index.values.tolist()
    # print(recommendations)
    return recommendations




