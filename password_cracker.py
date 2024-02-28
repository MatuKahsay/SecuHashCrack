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
    
def download_wordlist(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Assuming the wordlist is a text file, split it into lines
        return response.text.splitlines()
    else:
        logger.error(f"Failed to download wordlist from {url}. Status code: {response.status_code}")
        return None
    
def brute_force_attack(inputPass, algorithm, salt='', max_length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for password in itertools.product(chars, repeat=length):
            password = ''.join(password)
            if check_password(inputPass, password, algorithm, salt):
                return password
    return None  # If no password is found

def dictionary_attack(inputPass, algorithm, salt='', wordlist=None):
    for password in wordlist:
        if check_password(inputPass, password.strip(), algorithm, salt):
            return password.strip()
    return None  # If no password is found

def check_password(inputPass, password, algorithm, salt):
    password_attempts += 1
    password_with_salt = salt + password
    encPass = password_with_salt.encode("utf-8")
    hash_func = getattr(hashlib, algorithm, None)
    if hash_func:
        digest = hash_func(encPass).hexdigest()
        if digest == inputPass:
            return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Hash Cracker")
    parser.add_argument("hash", help="The hash to attempt to crack")
    parser.add_argument("--algorithm", help="The hashing algorithm (md5, sha1, sha256, sha512)", default="md5")
    parser.add_argument("--salt", help="Optional salt to prepend to each password attempt", default="")
    parser.add_argument("--wordlist_url", help="URL to download a wordlist from", default="")
    parser.add_argument("--wordlist_file", help="Path to the local wordlist file", default="")
    parser.add_argument("--attack_type", help="Type of attack to use (dictionary, brute_force)", default="dictionary")
    parser.add_argument("--max_length", help="Maximum password length for brute force attack", type=int, default=8)

    args = parser.parse_args()

    wordlist = None
    if args.wordlist_url:
        logger.info(f"Downloading wordlist from {args.wordlist_url}")
        wordlist = download_wordlist(args.wordlist_url)
    elif args.wordlist_file:
        logger.info(f"Using local wordlist file {args.wordlist_file}")
        try:
            with open(args.wordlist_file, "r") as file:
                wordlist = file.readlines()
        except FileNotFoundError:
            logger.error(f"Could not find wordlist file at {args.wordlist_file}.")
            return
    elif args.attack_type == "brute_force":
        logger.info("Using brute force attack.")
        result = brute_force_attack(args.hash, args.algorithm, args.salt, args.max_length)
        if result:
            logger.info(f"Password Found: {result}")
            return
        else:
            logger.info("Password not found.")
            return
    else:
        logger.error("No wordlist provided for dictionary attack.")
        return

    if args.attack_type == "dictionary":
        result = dictionary_attack(args.hash, args.algorithm, args.salt, wordlist)
        if result:
            logger.info(f"Password Found: {result}")
            return
        else:
            logger.info("Password not found.")
            return

if __name__ == '__main__':
    main()
