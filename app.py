'''
root module of the recommender app
'''
import pandas as pd
from flask import Flask, request, render_template
from recommendation import recommend_nmf, recommend_neighborhood
from utils import movies,  movie_title_search, movie_to_id, id_to_movie_title

#where we define our Flask object to be used to render our views
app = Flask(__name__) # __name__ defines this script as the root of our movieapp

# decorator that routes the function to a specified URL
@app.route('/')
def landing_page():
    '''
    User lands on this page and enters query
    '''
    return render_template('landing_page.html')

@app.route('/recommender/')
def recommender():
    '''
    queries accessed and transformed into recommendations
    '''
    print(request.args) # accesses the user query, prints in temrinal
    # example query for the .getlist method: ?q=star+wars&q=godfather&q=get+shorty
    # accesses the user query as a list
    
    model = request.args.get('models')

    try:

        user_query = request.args.getlist('movie')
    
   
        query = movie_title_search(user_query)
        query = movie_to_id(query)

        if model == 'nmf':
            recs = recommend_nmf(query, k=10)
        elif model == 'neighbor':
            recs = recommend_neighborhood(query, k=10)
        else:
            pass
        recommended= id_to_movie_title(recs)
        recommended= pd.DataFrame(recommended)
    except ValueError:
        print('The app only takes movie name')

    return render_template('recommender.html', recommended= recommended, model=model)

# parameterized URL
@app.route('/movie/<int:movieId>')
def movie_info(movieId):
    '''
    page for individual movie information
    '''
    movie=movies.set_index('movieId').loc[movieId]
    return render_template('movie_info.html', movie=movie, movieId=movieId) 


if __name__ == '__main__':
    # debug = True restarts servers after edits and prints verbose errors in terminal
    app.run(debug=True)
