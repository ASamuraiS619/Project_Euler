# -*- coding: utf-8 -*-

'''
Problem70 「トーティエント関数の置換」

オイラーのトーティエント関数 φ(n) (ファイ関数とも呼ばれる) とは, n 未満の正の整数で n と互いに素なものの個数を表す. 例えば, 1, 2, 4, 5, 7, 8 は9未満で9と互いに素であるので, φ(9) = 6 となる.
1 は全ての正の整数と互いに素であるとみなされる. よって φ(1) = 1 である.

面白いことに, φ(87109)=79180 であり, 87109は79180を置換したものとなっている.

1 < n < 10^7 で φ(n) が n を置換したものになっているもののうち, n/φ(n) が最小となる n を求めよ.
'''

import time
from functions import primes_up_to
from itertools import combinations

if __name__ == '__main__':
    start = time.time()

    # 素数はφ(n) = n-1 のため、n / φ(n)を最小とするものとしては有力だが、n-1はnの置換したものにはなり得ない。
    # よって次にn / φ(n)を最小とするものとして有力なn = p1 * p2(p1, p2は別の素数)を対象にして、
    # n / φ(n) かつ φ(n)がnの置換したものになっているかを調べ上げる。

    # √(10 ** 7) = 10 ** 3.5までだとn = p1 * p2が10 ** 7を大幅に下回る可能性があるので 2 * 10 ** 3.5までで。
    target_primes = primes_up_to(int(2 * 10 ** 3.5))
    minimum = 10
    answer = None
    for n, phi in ((p1 * p2, (p1 - 1) * (p2 - 1)) for p1, p2 in combinations(target_primes, 2) if p1 * p2 < 10 ** 7):
        value = n / phi
        if value < minimum and sorted(str(n)) == sorted(str(phi)):
            minimum, answer = value, n

    print(answer)   # answer 8319823

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.22288sec
