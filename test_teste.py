import unittest
import teste


class TestTeste(unittest.TestCase):

    def test_one_word(self):
        text = 'Testando'
        result = teste.palindrome(text)
        self.assertEqual(result, False)

    def test_multiple_words(self):
        text = 'Ara ara'
        result = teste.palindrome(text)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
