# -*- coding: utf-8 -*-

'''
Problem22 「名前のスコア」

5000個以上の名前が書かれている46Kのテキストファイル names.txt を用いる. まずアルファベット順にソートせよ.

のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.
たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある. またCOLINは 3 + 15 + 12 + 9 + 14 = 53 という値を持つ. よってCOLINは 938 × 53 = 49714 というスコアを持つ.
ファイル中の全名前のスコアの合計を求めよ.
'''

import time
import string

if __name__ == '__main__':
    start = time.time()

    alphabets = {}
    for index, char in enumerate(list(string.ascii_uppercase)):
        alphabets[char] = index + 1


    with open('p022_names.txt') as f:
        # テキストにもともとダブルクオーテーションが付いてしまっているので、取り除いてからsplitする。
        names = f.read().replace('"', '').split(',')
    names.sort()

    total_score = 0
    for index, name in enumerate(names):
        total_score += sum([alphabets[char] for char in list(name)]) * (index + 1)
    print(total_score)    # answer 871198282

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00816sec
