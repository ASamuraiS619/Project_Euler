# -*- coding: utf-8 -*-

'''
Problem2 「偶数のフィボナッチ数」

フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

数列の項の値が400万以下の, 偶数値の項の総和を求めよ.
'''


# 最初の2項を1, 1とすれば問題文の条件を満たしつつtotalの初期値に違和感が無いので便宜的に変更。

# a_n-2 初期値は1。
before_the_last_term = 1
# a_n-1 初期値は1。
last_term = 1
# a_n   初期値は2。
current_term = before_the_last_term + last_term

total = 0

while current_term < 4000000:
    if current_term % 2 == 0:
        total += current_term

    # 次に備えて項をずらす。
    before_the_last_term = last_term
    last_term = current_term
    current_term = before_the_last_term + last_term

# answer 4613732
print(total)
