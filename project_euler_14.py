# -*- coding: utf-8 -*-

'''
Problem14 「最長のコラッツ数列」

正の整数に以下の式で繰り返し生成する数列を定義する.
        n → n/2 (n が偶数)
        n → 3n + 1 (n が奇数)
13からはじめるとこの数列は以下のようになる.
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
13から1まで10個の項になる. この数列はどのような数字からはじめても最終的には 1 になると考えられているが, まだそのことは証明されていない(コラッツ問題)
さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.

注意: 数列の途中で100万以上になってもよい
'''

import time

def collatz_sequence_length(value, times=0):
    if value == 1:
        return times
    elif value % 2 == 0:
        return collatz_sequence_length(value // 2, times + 1)
    else:
        return collatz_sequence_length(value * 3 + 1, times + 1)

if __name__ == '__main__':
    start = time.time()

    max_sequence_length_index = 0
    max_sequence_length = 0
    for i in range(1, 1000001):
        sequence_length = collatz_sequence_length(i, 0)
        if sequence_length > max_sequence_length:
            max_sequence_length_index = i
            max_sequence_length = sequence_length

    print(max_sequence_length_index)    # answer 837799, length 525

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 3)) + "[sec]")   # 22.557sec
