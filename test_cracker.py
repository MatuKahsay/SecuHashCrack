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

    def test_brute_force_attack(self):
        # Using a known hash to test brute force attack
        known_hash = '5f4dcc3b5aa765d61d8327deb882cf99'  # This is the MD5 hash for 'password'
        self.assertEqual(brute_force_attack(known_hash, 'md5', max_length=8), 'password')
        # Test with non-existing password (should return None)
        self.assertIsNone(brute_force_attack('nonexistinghash', 'md5', max_length=3))

    def test_dictionary_attack(self):
        # Test dictionary attack with a known password list
        known_hash = '5f4dcc3b5aa765d61d8327deb882cf99'  # Again, the MD5 hash for 'password'
        wordlist = ['123456', 'password', 'admin']
        self.assertEqual(dictionary_attack(known_hash, 'md5', wordlist=wordlist), 'password')
        # Test with non-existing password in the wordlist
        self.assertIsNone(dictionary_attack(known_hash, 'md5', wordlist=['123456', 'admin']))

    def test_check_password(self):
        # Testing the password checking function directly
        self.assertTrue(check_password('5f4dcc3b5aa765d61d8327deb882cf99', 'password', 'md5'))
        self.assertFalse(check_password('5f4dcc3b5aa765d61d8327deb882cf99', 'wrongpassword', 'md5'))

if __name__ == '__main__':
    unittest.main()
