import unittest
from unittest.mock import patch
from password_cracker import evaluate_password_strength, download_wordlist, brute_force_attack, dictionary_attack, check_password


class TestPasswordCracker(unittest.TestCase):

    def test_evaluate_password_strength(self):
        # Test various password strengths
        self.assertEqual(evaluate_password_strength('1234'), 'Weak')
        self.assertEqual(evaluate_password_strength('StrongPass1!'), 'Strong')
        self.assertEqual(evaluate_password_strength('Moderate1'), 'Moderate')
