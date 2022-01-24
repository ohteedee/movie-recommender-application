# Movie-recommender-application
I desgned this flask application to recommend movies based on several models. So, its mostly a clustering project.  
The application takes users input and recommend movies that are either: similar to input movies, or simlar to movies other users see, or popular or random movies. 

Examples of algorithms that I used include ```k nearest neighbor``` which is the model that recommends based the type of movies seen by people who also saw your input movies and ``` non-negative matrix factorization algorithm``` which recommends movies that have similar features as your input movies.  



### Below is the recommender in action

![](movie_recommender.gif)

### Information about the files 
```app.py``` file is the main flask application file that contains all the the decorators needed to run and deploy the application. 
```recommendations.py``` contains functions to make rrecommendations with either of the four models used in the app. 
```utils.py``` contains functions imported into app.py. it contains code to load models, functions to take input and covert to movieId etc. 
```nmf_recommender.pkl``` is the nmf model that I generated generated. It is based on non negative matrix factorization algorithm. 
```neighbors_recommender.pkl``` is model generated based on nearest neighbor. 
The data folder contains the datasets used to generate the models. 
The notebooks folder contains jupyter notebook which I used to explore the dataset before creating a model. 
```requirements.txt``` contain information about dependencies needed to run the app. 
```Procfile``` is needed mainly for heroku deployment. it is not needed if you are just trying the app on your on local host. 
```runtime.txt```  is needed mainly for heroku deployment. it is not needed if you are just trying the app on your on local host
<br />

app designed by Tosin D. Oyewale (PhD)
[Linkedin](https://www.linkedin.com/in/tosin-oyewale/)



