# -*- coding: utf-8 -*-

'''
Problem22 「名前のスコア」

5000個以上の名前が書かれている46Kのテキストファイル names.txt を用いる. まずアルファベット順にソートせよ.

のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.
たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある. またCOLINは 3 + 15 + 12 + 9 + 14 = 53 という値を持つ. よってCOLINは 938 × 53 = 49714 というスコアを持つ.
ファイル中の全名前のスコアの合計を求めよ.
'''

import time

def score(name):
    name_in_index = map(lambda x: alphabets.index(x) + 1, name)
    value = sum(name_in_index)
    score = (names.index(name) + 1) * value
    return score

if __name__ == '__main__':
    start = time.time()

    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    with open('p022_names.txt') as f:
        # テキストにもともとダブルクオーテーションが付いてしまっているので、取り除いてからsplitする。
        names = f.read().replace('"', '').split(',')
    names.sort()

    total_score = sum(map(lambda x: score(x), names))
    print(total_score)    # answer 871198282

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.20171sec
