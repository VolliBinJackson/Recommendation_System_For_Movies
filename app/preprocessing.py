# This file prepares imports and data for the whole system

import pandas as pd

# below needed to show full column width and prevent the wrapping format

pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)


movies = pd.read_csv('../dataset/ml-latest-small/ml-latest-small/movies.csv')
ratings = pd.read_csv('../dataset/ml-latest-small/ml-latest-small/ratings.csv')

# Create new table that consists of user ratings for movies
user_movie_ratings = ratings.pivot_table(index='userId', columns='movieId', values='rating')

# Replace NaN with average from each column
user_movie_ratings = user_movie_ratings.fillna(user_movie_ratings.mean(axis=0))

print(user_movie_ratings.head())