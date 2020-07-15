# -*- coding: utf-8 -*-

'''
Problem25 「1000-digit Fibonacci number」

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
(フィボナッチ数列は、何項目で初めてに1000桁になるか。)
'''

import sys
import time

def fibonacchi_until_1000_digits(sequence):
    if len(str(sequence[-1])) == 1000:
        return len(sequence)
    else:
        sequence.append(sequence[-2] + sequence[-1])
        return fibonacchi_until_1000_digits(sequence)

if __name__ == '__main__':
    start = time.time()

    # 再帰上限数がデフォルトの1000では足りないので10000に書き換え。
    sys.setrecursionlimit(100000)
    index = fibonacchi_until_1000_digits([1, 1])
    print(index)    # answer 4782

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.02978sec

