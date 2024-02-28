import hashlib
import argparse
import logging
import time
import requests  # Import the requests library
import itertools
import string
import re  # Make sure to import the regex module

def evaluate_password_strength(password):
    """
    Evaluate the strength of a password.
    :param password: The password to evaluate.
    :return: A string describing the strength of the password.
    """
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_numbers = any(char.isdigit() for char in password)
    has_symbols = any(not char.isalnum() for char in password)
    complexity_score = sum([has_uppercase, has_lowercase, has_numbers, has_symbols])

    # Enhance weak passwords patterns with advanced regular expressions
    weak_patterns = [
        r'(.)\1+',  # Repeated characters like 'aaa', '1111', 'bbbbb', etc.
        r'1234',    # Simple sequences
        r'password', # Common weak passwords
        r'abc',    # Sequential letters
        # Add more patterns as needed.
    ]

    # Advanced password strength criteria
    if length < 8 or complexity_score < 3 or any(re.search(pattern, password, re.IGNORECASE) for pattern in weak_patterns):
        return 'Weak'
    elif 8 <= length < 12 and complexity_score >= 3:
        return 'Moderate'
    else:
        return 'Strong'