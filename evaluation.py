# This file is about the evaluation

import numpy as np
from sklearn.metrics import mean_squared_error
from app.collaborative_filtering import recommend_collaborative
from app.content_based_filtering import recommend_contend_based


def predict_ratings(user_id, movie_id):
    collab_recs = recommend_collaborative(user_id)
    content_recs = recommend_contend_based(movie_id)
    return np.mean([len(collab_recs), len(content_recs)])

ratings = [4.0, 3.5, 5.0, 2.0, 4.5]

predictions = []
for i in range(len(ratings)):
    user_id = i + 1
    movie_id = i + 1
    predicted_rating = predict_ratings(user_id, movie_id)
    predictions.append(predicted_rating)

mse = mean_squared_error(ratings, predictions)
print(f"Mean Squared Error: {mse}")