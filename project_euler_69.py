# -*- coding: utf-8 -*-

'''
Problem63 「Powerful digit counts」

オイラーのトーティエント関数, φ(n) [時々ファイ関数とも呼ばれる]は, n と互いに素な n 未満の数の数を定める. たとえば, 1, 2, 4, 5, 7, そして8はみな9未満で9と互いに素であり, φ(9)=6.

n	互いに素な数    φ(n)    n/φ(n)
2	1	            1       2
3	1,2	            2   	1.5
4	1,3         	2   	2
5	1,2,3,4     	4   	1.25
6	1,5         	2	    3
7	1,2,3,4,5,6	    6	    1.1666...
8	1,3,5,7	        4   	2
9	1,2,4,5,7,8 	6	    1.5
10	1,3,7,9	        4   	2.5
n ≤ 10 では n/φ(n) の最大値は n=6 であることがわかる.

n ≤ 1,000,000で n/φ(n) が最大となる値を見つけよ.
'''

import time
from functions import is_prime

# 素因数を多く持てば持つほどn/φ(n)は小さくなっていく。
# 素数を見つけるたびに掛けていき、100万を超えない最大の数字が答え。
if __name__ == '__main__':
    start = time.time()

    num = 2
    answer = 1
    while True:
        if is_prime(num):
            if answer * num > 10 ** 6:
                break
            else:
                print(num)
                answer *= num
        num += 1

    print(answer)   # answer 510510

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 9)) + "[sec]")   # 0.000082731sec
