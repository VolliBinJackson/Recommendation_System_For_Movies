import unittest
from app.hybrid_model import recommend_hybrid_model
from app.collaborative_filtering import recommend_collaborative
from app.content_based_filtering import recommend_contend_based

class TestHybridModel(unittest.TestCase):
    def test_hybrid_model(self):
        # test model with example User-ID and Movie-ID
        user_id = 1
        movie_id = 1
        result = recommend_hybrid_model(user_id, movie_id)
        self.assertIsInstance(result, list)  # expected pd.Series (not a list!)
        self.assertGreater(len(result), 0)  # at least one recommendation

        # Unlike both individual approaches: Check as well if hybrid model delivers at least as many recommendations as both individual models!
        self.assertGreaterEqual(len(result), max(len(recommend_collaborative(user_id)), len(recommend_contend_based(movie_id))))

if __name__ == '__main__':
    unittest.main()