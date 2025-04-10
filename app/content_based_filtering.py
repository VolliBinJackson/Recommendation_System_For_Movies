# This file uses Content-Based Filtering based on Genre

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import movies


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on Content-Based Filtering
def recommend_contend_based(movie_id, cosine_sim=cosine_sim):
    movie_idx = movies.index[movies['movieId'] == movie_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[movie_idx]))

    # sort movies based on similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # selects movies (excluding self) from 1 to a desired amount (flexible, in this case 5 movies)
    sim_scores = sim_scores[1:6]

    # fetch movie ID's
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]



