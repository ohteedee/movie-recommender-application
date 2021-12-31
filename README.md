# movie-recommender-application
This is flask application that recommends movies based on several models to users. 

it takes users input and recommend movies that are either: similar to inoput movies, or simlar to movies other users see, or popular or random movies. 


### Below is the recommender in action

![](movie_recommender.gif)

### information about the files 
app.py is the main flsk application file that contains all the the decorators needed to run and deploy the application.
recommendations.py contains functions to make rrecommendations with either of the four models used in the app
utils.py contains functions imported into app.py. it contains code to load models, functions to take input and covert to movieId etc
nmf_recommender.pkl is the nmf generated. it is based on non negative matrix factorization algorithm
neighbors_recommender.pkl is model generated based on nearest neighbor 
data folder contains the datasets used to generate the models.
notebooks folder contains jupyter notebook 
requirements.txt contain information about dependencies needed to run the app. 
Procfile is needed mainly for heroku deployment. it unnecessary to try the app on local host flask
runtime.txt  is needed mainly for heroku deployment. it unnecessary to try the app on local host flask

app designed by Tosin D. Oyewale (PhD)



