# -*- coding: utf-8 -*-

'''
Problem39 「Integer right triangles」

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
(直角三角形の周の長さpを1000以下で変化させた時に、3辺の組み合わせが最も多くなるpを求めよ。)
'''

import time


if __name__ == '__main__':
    start = time.time()

    # 毎回計算しなくて良いように、平方数の辞書を作っておく。
    # 最高でもどの辺も500未満なので、499までで作っておけば十分。
    squares = {num: num ** 2 for num in range(1, 500)}

    answer_solutions = None
    answer_length = 0
    answer = None

    # pの最小は{3, 4, 5}のときの12なのでそこからスタート
    # どのような組み合わせでもpは必ず奇数になる
    for p in range(12, 1001, 2):
        solutions = []
        # a < b < cとして解いている。(同じ長さの辺は存在し得ない。)
        # 整数の範囲ではa = 1にはなり得ない。
        # c < a + bが必要な条件で、これとa < b < cとc = p - (a+b)を合わせると
        # a >= p / 4のとき、 a < b < (p-a) / 2
        # a < p / 4のとき、 p/2 - a < b < (p-a) / 2 となる。
        for a in range(2, p // 3):
            if a >= p // 4:
                b_min = a + 1
            else:
                b_min = (p // 2) - a + 1
            for b in range(b_min, (p-a) // 2):
                c = p - (a+b)
                if squares[a] + squares[b] == squares[c]:
                    solutions.append((a, b, c))

        if len(solutions) > answer_length:
            answer_solutions = solutions
            answer_length = len(solutions)
            answer = p

    print(answer_solutions)
    print(answer_length)
    print(answer)   # answer 840

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.99732sec
