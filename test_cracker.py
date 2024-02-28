import unittest
from unittest.mock import patch
from password_cracker import evaluate_password_strength, download_wordlist, brute_force_attack, dictionary_attack, check_password


class TestPasswordCracker(unittest.TestCase):

    def test_evaluate_password_strength(self):
        # Test various password strengths
        self.assertEqual(evaluate_password_strength('1234'), 'Weak')
        self.assertEqual(evaluate_password_strength('StrongPass1!'), 'Strong')
        self.assertEqual(evaluate_password_strength('Moderate1'), 'Moderate')

        @patch('requests.get')
    def test_download_wordlist(self, mock_get):
        # Mocking requests.get to test wordlist download functionality
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'password\n123456\nadmin'
        self.assertEqual(download_wordlist('http://example.com'), ['password', '123456', 'admin'])
        mock_get.return_value.status_code = 404
        self.assertIsNone(download_wordlist('http://example.com'))
