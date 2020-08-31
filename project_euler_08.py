# -*- coding: utf-8 -*-

'''
Problem8 「数字列中の最大の積」

次の1000桁の数字のうち, 隣接する4つの数字の総乗の中で, 最大となる値は, 9 × 9 × 8 × 9 = 5832である.
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
この1000桁の数字から13個の連続する数字を取り出して, それらの総乗を計算する. では、それら総乗のうち、最大となる値はいくらか.

EX 6桁の数123789から5個の連続する数字を取り出す場合, 1*2*3*7*8と2*3*7*8*9の二通りとなり, 後者の2*3*7*8*9=3024が最大の総乗となる.
'''

import time

if __name__ == '__main__':
    start = time.time()

    target = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

    # for文で回せるよう文字列へ
    target_str = str(target)

    largest_multiple = 1

    for i in range(len(target_str) - 12):
        tmp_list = target_str[i:i+13]
        tmp_multiple = 1
        for k in tmp_list:
            tmp_multiple *= int(k)
        if tmp_multiple > largest_multiple:
            largest_multiple = tmp_multiple

    print(largest_multiple)     # answer 23514624000

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00346sec
