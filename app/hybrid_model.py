from collaborative_filtering import recommend_collaborative
from content_based_filtering import recommend_contend_based

# Hybrid model that combines recommendations from both approaches (Collaboratie + Content-Based)

def recommend_hybrid_model(user_id, movie_id, alpha=0.5):
    collab_recs = recommend_collaborative(user_id)
    content_recs = recommend_contend_based(movie_id)
    combined_recs = list(set(collab_recs).union(set(content_recs)))
    return combined_recs

combined = recommend_hybrid_model(1, 1)
print("Hybrid model:")
print(combined)