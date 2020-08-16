# -*- coding: utf-8 -*-

'''
Problem59 「XOR decryption」

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
(p_59_cipher.txtをXOR解読し、得られた英文の文字を全てASCIIコードへ変換したものの合計を求めよ。)
'''

import time
import string
from itertools import product


def decrypt(cipher, password):
    password_ascii = list(map(ord, password))
    cipher_decrypted_ascii = [num ^ password_ascii[index % 3] for index, num in enumerate(cipher)]
    cipher_decrypted_letters = list(map(chr, cipher_decrypted_ascii))
    return ''.join(cipher_decrypted_letters), cipher_decrypted_ascii

if __name__ == '__main__':
    start = time.time()

    password_options = product(string.ascii_lowercase, repeat=3)

    with open('p059_cipher.txt') as f:
        cipher = list(map(int, f.read().strip().split(',')))
        for password in password_options:
            decrypted_letters, decrypted_ascii = decrypt(cipher, password)
            if (decrypted_letters.find('The ') != -1 or decrypted_letters.find(' the ') != -1) and decrypted_letters.find(' of ') != -1:
                # print(password, decrypted_letters)
                print(sum(decrypted_ascii))     # answer 129448
                break

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.75334sec
