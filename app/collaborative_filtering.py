# This file uses collaborative_filtering function which
# uses k-NN model for User-User Collaborative Filtering

from sklearn.neighbors import NearestNeighbors
from preprocessing import user_movie_ratings, movies

model = NearestNeighbors(n_neighbors=5, algorithm='auto', metric='cosine')
model.fit(user_movie_ratings.fillna(0))


# Function to give movie recommendations for a specific user
def recommend_collaborative(user_id):
    if not user_id in user_movie_ratings:
        return "User does not exist."

    # finding the k-next neighbors (i.e. similar users)
    distances, indices = model.kneighbors(user_movie_ratings.loc[user_id].values.reshape(1, -1))

    # fetch movies the similar users have watched
    recommended_movie_ids = user_movie_ratings.columns[indices.flatten()]
    recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]['title']
    return recommended_movies


userId = 1
recommended_collab = recommend_collaborative(userId)
print("Collaborative Filtering:")
print(recommended_collab)


