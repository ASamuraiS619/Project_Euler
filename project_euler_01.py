# -*- coding: utf-8 -*-

'''
Problem1 「3と5の倍数」

10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.

同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
'''

proper_numbers = []

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        proper_numbers.append(i)

# answer 233168
print(sum(proper_numbers))
