# Recommendation_System_For_Movies

This is my personal project to learn, practice and get familiar with Machine Learning, Unit Testing and web deployment. 

# Overview

This project implements a movie recommendation system using a **hybrid approach** that combines **Collaborative Filtering** and **Content-Based Filtering** to generate personalized suggestions. 

# Dataset

It leverages the popular MovieLens dataset (https://grouplens.org/datasets/movielens/latest/) and simulates a recommender engine similar to those used by platforms like Netflix or Amazon Prime. It is widely used in research to develop and test recommendation algorithms.

This project used the MovieLens 100k dataset, which contains over 100,000 reviews from users on movies.

Important files in the dataset:
- ratings.csv: Contains user reviews. Each line represents a rating from a user about a movie (User ID, Movie ID, Rating, Timestamp).
- movies.csv: Contains the metadata of the movies (Movie ID, Movie Title, Genre).


# Methods Used

The recommendation engine combines the strengths of both filtering techniques:

Collaborative Filtering
- **User-Based Collaborative Filtering**: Assumes users with similar rating patterns will enjoy similar movies. User similarity is calculated using cosine similarity.
- **Item-Based Collaborative Filtering**: Assumes that if a user liked movie A, they might also like movie B, based on ratings from other users.

Content-Based Filtering
- Focuses on the **attributes of the movies themselves** (e.g., genre, title).
- The system computes **cosine similarity** between movies based on genre metadata and suggests similar items.
- This is especially useful for new users (cold start) or when historical user data is sparse.

The final **hybrid model** combines both approaches for improved accuracy.

# Goal of the Project 

To build a working recommendation system that:
- Suggests movies based on user preferences
- Combines collaborative filtering and content similarity
- Runs as an interactive web app using Streamlit
- Includes basic unit tests for core components

# Running the Project

1. Clone the repo:  ```bash
                    git clone <repo-link>
                    cd Recommendation_System_For_Movies

3. create venv (recommended): python -m venv .venv
                              .venv\Scripts\activate # on Windows
                              source .venv/bin/activate # on Linux/Mac

4. Install dependencies:  pip install -r requirements.txt

5. Run the webserver: cd app
                      streamlit run main.py    

