# -*- coding: utf-8 -*-

'''
Problem66 「ディオファントス方程式」

次の形式の, 2次のディオファントス方程式を考えよう:

x^2 - Dy^2 = 1
たとえば D=13 のとき, x を最小にする解は 649^2 - 13×180^2 = 1 である.

D が平方数(square)のとき, 正整数のなかに解は存在しないと考えられる.

D = {2, 3, 5, 6, 7} に対して x を最小にする解は次のようになる:

3^2 - 2×2^2 = 1
2^2 - 3×1^2 = 1
9^2 - 5×4^2 = 1
5^2 - 6×2^2 = 1
8^2 - 7×3^2 = 1
したがって, D ≤ 7 に対して x を最小にする解を考えると, D=5 のとき x は最大である.

D ≤ 1000 に対する x を最小にする解で, x が最大になるような D の値を見つけよ.
'''

import time
from project_euler_64 import next_fraction
from project_euler_65 import expandion_of_continued_fraction

# Problem64のcontinued_fraction_periodを、循環ブロックも返すように改良。
def continued_fraction_block_and_period(square_root_content, fraction_sequence, block):
    if len(fraction_sequence) == 0:
        fraction_sequence.append((1, square_root_content, int(square_root_content ** 0.5)))
        block.append(int(1 / (square_root_content ** 0.5 - int(square_root_content ** 0.5))))
        return continued_fraction_block_and_period(square_root_content, fraction_sequence, block)

    if len(fraction_sequence) != 1 and fraction_sequence[-1] == fraction_sequence[0]:
        return len(fraction_sequence) - 1, block[:-1]
    else:
        fraction_sequence.append(next_fraction(fraction_sequence[-1]))
        a, b, c = fraction_sequence[-1]
        block.append(int(a / (b ** 0.5 - c)))
        return continued_fraction_block_and_period(square_root_content, fraction_sequence, block)


if __name__ == '__main__':
    start = time.time()

    largest_x = 0
    answer = 0
    for d in range(2, 1001):
        if (d ** 0.5).is_integer():
            continue
        period, block = continued_fraction_block_and_period(d, [], [])
        # まず、循環ブロックの最後の1つを除いたところまで連分数を仮分数化する。
        expandion = expandion_of_continued_fraction(block[:-1])
        x1 = expandion.numerator
        y1 = expandion.denominator
        # 上記のx1, y1について、今回のディアフォントス方程式(ペル方程式とも言うらしい)の解は
        # 周期が偶数の時: x = x1, y = y1
        # 周期が奇数の時: x + y√D = (x1 + y1√D)^2となることから、x = x1^2 + d * y1^2, y = 2 * x1 * y1
        if period % 2 == 0:
            x = x1
        else:
            x = x1 ** 2 + d * y1 ** 2
        if x > largest_x:
            largest_x = x
            answer = d

    print(answer)   # answer 661

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.06248sec
