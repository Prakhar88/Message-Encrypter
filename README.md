Text Encryption & Decryption Toolkit
A Python-based command-line tool that provides multiple classical encryption and decryption methods for text processing. This toolkit implements five different cipher algorithms with an interactive menu system.
Features
The toolkit supports the following encryption methods:
1. Atbash Cipher

Reverses the alphabet (A↔Z, B↔Y, etc.)
Preserves case and non-alphabetic characters
Symmetric operation (encryption = decryption)

2. Alphanumeric Cipher

Converts alphabetic characters to their position numbers (A=1, B=2, etc.)
Uses hyphens as separators between numbers
Preserves non-alphabetic characters in original positions

3. Caesar Cipher

Shifts each letter by 3 positions in the alphabet
Classic implementation with wrap-around
Preserves case and non-alphabetic characters

4. ROT-n Cipher

Customizable rotation cipher (user-defined shift value)
Similar to Caesar but with variable shift amount
Maintains original text structure with non-alphabetic characters

5. Vigenère Cipher

Polyalphabetic substitution using a keyword
Key repeats to match text length
Validates key to contain only alphabetic characters
Advanced security through keyword-based encryption

Installation

Clone this repository:

bashgit clone https://github.com/yourusername/text-encryption-toolkit.git
cd text-encryption-toolkit

Ensure you have Python 3.x installed on your system.
Run the main program:

bashpython Encryption.py
Usage
Running the Program
Execute the main script to start the interactive menu:
bashpython Encryption.py
Menu Options

Encrypt - Choose from 5 encryption methods
Decrypt - Decrypt using the corresponding method
Exit - Close the program

Example Usage
Welcome to text encrypter and decrypter
1.Encrypt
2.Decrypt
3.exit
enter choice: 1

enter the message below:
Hello World!

Enter the type of encryption you want?
1. Atbash (Flips around the alphabets)
2. Alphanumeric (turns alphabets into number)
3. Caesar(not the salad) (shifts the alphabet ahead by 3)
4. Rotation_n (Rotates the message by n characters)
5. Vigenere (encrypt using a key)
enter choice: 1

Svool Dliow!
File Structure
├── Encryption.py      # Main program with interactive menu
├── Abtash.py         # Atbash cipher implementation
├── Alphanum.py       # Alphanumeric cipher implementation
├── Ceasar.py         # Caesar cipher implementation
├── ROT_n.py          # ROT-n cipher implementation
├── Vigenere.py       # Vigenère cipher implementation
└── README.md         # This file
Cipher Details
Atbash Cipher

Algorithm: Maps each letter to its mirror position in the alphabet
Example: "Hello" → "Svool"
Note: Encryption and decryption use the same function

Alphanumeric Cipher

Algorithm: Converts letters to numbers (A/a=1, B/b=2, etc.)
Example: "Hello" → "8-5-12-12-15"
Format: Numbers separated by hyphens

Caesar Cipher

Algorithm: Shifts each letter 3 positions forward (encryption) or backward (decryption)
Example: "Hello" → "Khoor"
Wrap-around: Z shifts to C, A shifts back to X

ROT-n Cipher

Algorithm: User-defined rotation amount
Example: "Hello" with n=5 → "Mjqqt"
Interactive: Prompts for rotation value

Vigenère Cipher

Algorithm: Uses a repeating keyword to shift letters variably
Example: "Hello" with key "KEY" → "Rijvs"
Security: More secure than simple substitution ciphers
Validation: Ensures key contains only alphabetic characters

Error Handling
The program includes robust error handling for:

Invalid menu choices
Non-numeric input where numbers are expected
Invalid keys for Vigenère cipher
Key length validation for Vigenère cipher

Technical Notes

All ciphers preserve the case of original text
Non-alphabetic characters (spaces, punctuation, numbers) remain unchanged
The program uses ASCII values for character manipulation
Modular arithmetic ensures proper wrap-around for alphabet boundaries

Educational Purpose
This toolkit is designed for educational purposes to demonstrate classical cryptography techniques. These ciphers are not suitable for securing sensitive information in real-world applications.
Contributing
Feel free to contribute by:

Adding new cipher algorithms
Improving the user interface
Adding file input/output capabilities
Implementing additional security features
