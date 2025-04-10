import unittest
import pandas as pd

from app.content_based_filtering import recommend_contend_based

class TestContentBasedFiltering(unittest.TestCase):
    def test_recommend_content_based(self):
        user_id = 1
        result = recommend_contend_based(user_id)
        self.assertIsInstance(result, pd.Series)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()