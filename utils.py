
'''
import data here and have utility functions that could help
'''

import pandas as pd
import pickle
from thefuzz import fuzz, process

ratings = pd.read_csv('./data/ml-latest-small/ratings.csv')
movies =  pd.read_csv('./data/ml-latest-small/movies.csv')


# import nmf model
with open('./nmf_recommender.pkl', 'rb') as file:
        nmf_model = pickle.load(file)

# import neighborhood model
with open('./neighbors_recommender.pkl', 'rb') as file:
        neighbor_model = pickle.load(file)

def movie_title_search(fuzzy_titles):
    '''
    does a fuzzy search and returns best matched movie
    '''
    extracted_titles =[]
    choices = movies['title'].tolist()
    for fuzzy_title in fuzzy_titles:
        extracted_title =process.extract(fuzzy_title, choices, limit=1)
        extracted_title = extracted_title[0][0]
        extracted_titles.append(extracted_title)
    return extracted_title
        


def movie_to_id(extracted_titles):
    '''
    converts movie title to id for use in algorithms
    '''
    movieId = movies.set_index('title').loc[extracted_titles].movieId
    movieId = movieId.tolist()
    return movieId

def id_to_movie_title(movieId):
    '''
    converts movie Id to title
    '''
    title_genre_df = movies.set_index('movieId').loc[movieId]
    recommendations_title = title_genre_df.title
    return recommendations_title 