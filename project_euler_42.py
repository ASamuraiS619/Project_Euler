# -*- coding: utf-8 -*-

'''
Problem42 「Coded triangle numbers」

The nth term of the sequence of triangle numbers is given by, t(n) = ½n(n+1); so the first ten triangle numbers are:

        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
(p042_words.txtの単語について、アルファベット番号の合計が三角数になる単語はいくつあるか？)
'''

import time
import string

# 条件を満たす単語をtriangle_wordと呼ぶこととする。
def is_triangle_word(word):
    word = word.upper()
    _sum = sum([ALPHABETS_DICT[char] for char in word])
    if _sum in triangle_numbers:
        return True
    else:
        return False

if __name__ == '__main__':
    start = time.time()

    ALPHABETS = string.ascii_uppercase
    ALPHABETS_DICT = {alphabet: (index + 1) for index, alphabet in enumerate(ALPHABETS)}
    # ダブルクオーテーションを0点にすることで、words.textからダブルクオーテーションを除く工程をカット。
    ALPHABETS_DICT['"'] = 0

    triangle_numbers = set([n * (n + 1) / 2 for n in range(1, 20)])

    answer = 0
    with open('p042_words.txt') as f:
        words = f.read().strip().split(',')
        for word in words:
            if is_triangle_word(word):
                answer += 1

    print(answer)   # answer 162

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00231sec
