#importing the required libraries for the task
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hvplot.pandas
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#importing the dataset into the workspace
data = pd.read_csv('D:\Machine Learning with Python\MOVIE RECOMMENDATION SYSTEM FOR SEMINAR - I\movies.csv')

#selecting the features for building the recommendation system
selecting_features = ['genres','keywords','tagline','cast','director']

# filling the null values with ' ' in the selected features
for feature in selecting_features:
    data[feature] = data[feature].fillna('')

#combining all features of every row into single string
combine_feat = data['genres']+' '+data['keywords']+' '+data['tagline']+' '+data['cast']+' '+data['director']

#using TfidfVectorizer() for converting text into feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combine_feat)

# finding the similarity between all columns among each other
similarity = cosine_similarity(feature_vectors)


# Recommendation System
movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = data[data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = data[data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1