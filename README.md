# SecuHashCrack

This Python project provides tools for cracking hashed passwords through various techniques, including brute force attacks and dictionary attacks. It supports multiple hashing algorithms and allows for the inclusion of salts. Additionally, the program can evaluate the strength of a password based on several criteria.

## Features

- **Password Strength Evaluation**: Analyzes a password's strength based on its length, use of uppercase and lowercase letters, digits, and symbols, as well as common weak patterns.
- **Wordlist Downloading**: Downloads a wordlist from a specified URL for use in dictionary attacks.
- **Brute Force Attack**: Attempts to crack a hash by trying all possible combinations up to a specified length.
- **Dictionary Attack**: Attempts to crack a hash using a list of known passwords.
- **Support for Salts**: Can prepend a salt to each password attempt, supporting systems that use salted hashes.
- **Multiple Hashing Algorithms**: Supports `md5`, `sha1`, `sha256`, and `sha512` hashing algorithms.

## Installation

1. Ensure you have Python installed on your system.
2. Clone the repository or download the source code.
3. Install required dependencies by running `pip install -r requirements.txt` in the terminal.

## Usage

The program can be run from the command line, providing various arguments to specify the hash, algorithm, attack type, and other options.

### Basic Command Structure

'python password_cracker.py <hash> [options]'

### Options

    --algorithm: Specify the hashing algorithm (md5, sha1, sha256, sha512). Default is md5.
    --salt: Optional salt to prepend to each password attempt.
    --wordlist_url: URL to download a wordlist from for dictionary attacks.
    --wordlist_file: Path to a local wordlist file for dictionary attacks.
    --attack_type: Type of attack to use (dictionary, brute_force). Default is dictionary.
    --max_length: Maximum password length for brute force attacks. Default is 8.

 ## Examples

Cracking a hash with a dictionary attack using a local wordlist file:

```bash
python password_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist_file /path/to/wordlist.txt

Performing a brute force attack on a hash:


```bash
python password_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 --attack_type brute_force --max_length 6

### Development and Testing

The project includes a test suite to verify the functionality of its components. Run the tests using:

```bash
python -m unittest test_cracker.py

 ### Contributing

Contributions to improve the project are welcome. Please follow the standard GitHub pull request process to propose changes.
License

This project is open-sourced under the MIT License. See the LICENSE file for more details.



