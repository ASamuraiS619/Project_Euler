# -*- coding: utf-8 -*-

'''
Problem27 「Number spiral diagonals」

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

[21] 22  23  24  [25]
 20 [ 7]  8 [ 9]  10
 19   6 [ 1]  2   11
 18 [ 5]  4 [ 3]  12
[17] 16  15  14  [13]

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
(上記のように数字を並べた1001 × 1001 の四角形の両対角線上の数字の合計を求めよ。)
'''

import time

# 1辺の長さは奇数しか取れない。
# 長さnの正方形の右上の数字は n ** 2
# 長さnの正方形の一番外側の四隅の合計は、一回り小さい正方形の右上の数字が(n-2) ** 2なので、
# (n-2) ** 2 + (n-1) (右下) + (n-2) ** 2 + 2(n-1) (左下) + (n-2) ** 2 + 3(n-1) (左上) + (n-2) ** 2 + 4(n-1) (右上)
# 足し合わせると 4 * (n-2) ** 2 + 10 * (n-1)
# これを、最初の1に必要な回数足し合わせればOK

def diagonal_sum(length):
    if length == 1:
        return 1
    elif length < 1 or length % 2 == 0:
        return None
    else:
        _sum = 1
        for n in range(3, length + 1, 2):
            _sum += 4 * (n-2) ** 2 + 10 * (n-1)
        return _sum

if __name__ == '__main__':
    start = time.time()

    print(diagonal_sum(10001))   # answer 669171001

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 8)) + "[sec]")   # 0.00030112sec

