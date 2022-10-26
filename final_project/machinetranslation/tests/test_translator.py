"""
This module tests translation from English to French and vice versa.
"""
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    This class unit tests translator module functions english_to_french and french_to_english
    """
    def test_english_to_french(self):
        """
        This function tests translation from english to french
        """
        self.assertEqual(english_to_french(None), None) # test when null is given as input the output is null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertNotEqual(english_to_french(None), '') # test when null is given as input the output is not empty string.
        self.assertNotEqual(english_to_french('Hello'), 'Hello') # test when 'Hello' is given as input the output is not 'Hello'.

    def test_french_to_english(self):
        """
        This function tests translation from french to english
        """
        self.assertEqual(french_to_english(None), None) # test when null is given as input the output is null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertNotEqual(french_to_english(None), '') # test when null is given as input the output is not empty string.
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour') # test when 'Bonjour' is given as input the output is not 'Bonjour'.

if __name__ == '__main__':
    unittest.main()
