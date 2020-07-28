# -*- coding: utf-8 -*-

'''
Problem2 「偶数のフィボナッチ数」

フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

数列の項の値が400万以下の, 偶数値の項の総和を求めよ.
'''


import time

def fibonacci_sequence(threshold, sequence=[1, 1]):
    if sequence[-1] > threshold:
        return sequence
    else:
        sequence.append(sequence[-2] + sequence[-1])
        return fibonacci_sequence(threshold, sequence)

if __name__ == '__main__':
    start = time.time()

    THRESHOLD = 4 * 10 ** 6
    target_sequence = fibonacci_sequence(THRESHOLD)

    print(sum([num for num in target_sequence if num % 2 == 0]))

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 10)) + "[sec]")   # 0.000056028sec
