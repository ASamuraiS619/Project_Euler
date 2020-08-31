# -*- coding: utf-8 -*-

'''
Problem9 「特別なピタゴラス数」

ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.

                a^2 + b^2 = c^2

例えば, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 である.
a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい.
'''

import time

if __name__ == '__main__':
    start = time.time()

    # a < b < cとして考える。
    flag = False
    for a in range(3, 1000 // 3 + 1):
        for b in range(a+1, (1000-a) //2 + 1):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)    # answer 31875000
                flag = True
                break
        if flag == True:
            break

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.06115sec
