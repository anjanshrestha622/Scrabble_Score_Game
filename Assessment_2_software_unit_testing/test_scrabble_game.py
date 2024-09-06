import unittest
from scrabble_score import compute_score, choose_random_word_of_length


class TestScrabbleScore(unittest.TestCase):
    """
    Test class for Scrabble score and word selection functionality.
    """

    def test_word_scoring(self):
        """Test the score calculation for different words."""
        self.assertEqual(compute_score('cat'), 5)
        self.assertEqual(compute_score('quiz'), 22)
        self.assertEqual(compute_score('xylophone'), 24)

    def test_invalid_word(self):
        """Test handling of invalid words."""
        self.assertEqual(compute_score('*'), 0)

    def test_choose_random_word_of_length(self):
        """Test random word selection based on length."""
        word = choose_random_word_of_length(3)
        self.assertIn(word, ["cat", "dog", "bat", "rat"])


if __name__ == '__main__':
    unittest.main()
