import unittest
from src.utils.preprocessing import normalize_data, handle_missing_values, extract_features

class TestPreprocessing(unittest.TestCase):

    def test_normalize_data(self):
        data = [[1, 2], [3, 4], [5, 6]]
        normalized = normalize_data(data)
        expected = [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]]
        self.assertEqual(normalized, expected)

    def test_handle_missing_values(self):
        data = [[1, 2], [None, 4], [5, None]]
        handled = handle_missing_values(data)
        expected = [[1, 2], [3, 4], [5, 3]]
        self.assertEqual(handled, expected)

    def test_extract_features(self):
        raw_data = [[1, 2, 3], [4, 5, 6]]
        features = extract_features(raw_data)
        expected_features = [[1, 2], [4, 5]]
        self.assertEqual(features, expected_features)

if __name__ == '__main__':
    unittest.main()