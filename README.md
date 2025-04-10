# Recommendation_System_For_Movies

This is my own project to learn, practice and get familiar with Machine Learning, Unit Testing and hosting. 

# Overview

This project includes a film recommendation system that works with modern methods of collaborative filtering to generate personalized recommendations for films. Recommendations are based on users' ratings and preferences, and the model uses historical interactions to identify patterns and make predictions. This system could be used on a platform such as Netflix, Amazon Prime, or a similar service to suggest relevant movies to users.

The system uses the popular MovieLens dataset and is a simple but effective example of applying machine learning to recommender systems.

# Dataset

The dataset I used is the MovieLens dataset, which contains a collection of ratings and metadata about movies. It is widely used in research to develop and test recommendation algorithms.

Here is the link: https://grouplens.org/datasets/movielens/latest/ 

This project used the MovieLens 100k dataset, which contains over 100,000 reviews from users on movies.

Important files in the dataset:
movies.csv: Contains user reviews. Each line represents a rating from a user about a movie (User ID, Movie ID, Rating, Timestamp).

movies.csv: Contains the metadata of the movies (Movie ID, Movie Title, Genre).

# Goal of the Project 

The goal of this project is to develop a recommendation model that suggests movies for a user based on their ratings and the reviews of similar users. The main approach we use is collaborative filtering. We implement both user-assisted and item-based collaborative filtering. Approaches and methods The system uses two main approaches to collaborative filtering: 

- User-assisted collaborative filtering: This approach is based on the assumption that similar users like similar movies. Similarities between users are calculated, and recommendations are made based on that. Similarity between users is measured using metrics such as cosine similarity.
- Item-based collaborative filtering: This approach assumes that movies that have been highly rated by similar users might also appeal to a specific user.

Both approaches get combined and it becomes a hybrid model, which we use for our webserver.
