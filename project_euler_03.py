# -*- coding: utf-8 -*-

'''
Problem3 「最大の素因数」

13195 の素因数は 5, 7, 13, 29 である.
600851475143 の素因数のうち最大のものを求めよ.
'''

import time

if __name__ == '__main__':
    start = time.time()

    target = 600851475143
    THRESHOLD = int(target ** 0.5)    # 775146
    for num in range(3, THRESHOLD, 2):
        if target == num:
            answer = num
        while target % num == 0:
            target /= num

    print(answer)   # answer 6857

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.06638sec
