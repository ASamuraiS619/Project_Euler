# -*- coding: utf-8 -*-

'''
Problem38 「Pandigital multiples」

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
(ある数に1, 2, … , Nをかけた数順に結合したら1〜9のパンデジタル数になる場合、そのパンデジタル数で最大のものを答えよ。)
'''

# ① 9が918273645というパンデジタル数となる以上、元となる数は桁の先頭が9から始まる数字
# ② N=4で、(2桁) + (2桁) + (2桁) + (3桁) は、①より乗数が2の時に3桁になってしまうので不可。
# ③ N=3で、(3桁) + (3桁) + (3桁) も同様に乗数が2の時に4桁になってしまうので不可。
# ④ N=2で、(4桁) + (5桁) のみ条件に合致し得る。(9のパンデジタル数が918273645なので9182以上。)
# ⑤ 9500以上の数字を2倍すると19◯◯◯となり9が被るので、求める数は9182以上9499以下にあるはず。

import time

if __name__ == '__main__':
    start = time.time()

    largest_pandigital = 0
    for multiplicand in range(9182, 9500):
        # もしかけられる数が既にパンデジタルでなければ(桁の数字が被っていたら)検査しない。
        if len(set(str(multiplicand))) != 4:
            pass
        elif set(str(multiplicand) + str(multiplicand * 2)) == set([str(multiplicand) for multiplicand in range(1, 10)]):
            largest_pandigital = int(str(multiplicand) + str(multiplicand * 2))

    print(largest_pandigital)   # answer 932718654

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00092sec
