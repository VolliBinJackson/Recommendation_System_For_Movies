import unittest
import pandas as pd
from app.collaborative_filtering import recommend_collaborative

class TestCollaborativeFiltering(unittest.TestCase):
    def test_recommend_collaborative(self):
        user_id = 1
        result = recommend_collaborative(user_id)
        self.assertIsInstance(result, pd.Series)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()