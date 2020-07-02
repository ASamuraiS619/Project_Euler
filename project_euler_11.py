# -*- coding: utf-8 -*-

'''
Problem11 「格子内の最大の積」

上の 20×20 の格子のうち, 斜めに並んだ4つの数字が赤くマークされている.
(以下で[]の付いているもの)

08 02 22 97 38 15 00 40  00  75  04  05  07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57  60  87  17  40  98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29  93  71  40  67  53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42  69  24  68  56  01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89  41  92  36  54  22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02  44  75  33  53  78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 [26] 38  40  67  59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20  95 [63] 94  39  63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26  97  17 [78] 78  96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44  20  45  35 [14] 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67  15  94  03  80  04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47  55  58  88  24  00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07  05  44  44  37  44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69  28  73  92  13  86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16  07  97  57  32  16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72  03  46  33  67  46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11  24  94  72  18  08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88  34  62  99  69  82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01  74  31  49  71  48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69  16  92  33  48  61 43 52 01 89 19 67 48

それらの数字の積は 26 × 63 × 78 × 14 = 1788696 となる.
上の 20×20 の格子のうち, 上下左右斜めのいずれかの方向で連続する4つの数字の積のうち最大のものはいくつか?
'''

import re
import numpy as np

# 横方向に4つ連続する数字の積について、全パターンを配列で返す。
def multiples_in_line_by_4(array):
    multiples = []
    for i in range(len(array)):
        for k in range(len(array[i]) - 3):
            multiples.append(array[i][k:k+4].prod())

    return multiples


target_matrix = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

if __name__ == '__main__':
    # まずは文字列で1次元の配列に
    str_matrix_in_row = re.split('[ \n]', target_matrix)
    # 要素を全てint型に
    matrix_in_row = list(map(lambda x: int(x), str_matrix_in_row))
    # ndarrayへ変換
    target_array_in_row = np.array(matrix_in_row)
    target_array = np.reshape(target_array_in_row, (20, 20))

    horizontal_multiples = multiples_in_line_by_4(target_array)

    # taret_arrayを転置してmultiples_in_line_by_4で積を取得。
    vertical_multiples = multiples_in_line_by_4(target_array.T)

    # 右斜下方向の積一覧
    right_diagonal_multiples = []
    for i in range(len(target_array) - 3):
        for k in range(len(target_array[i]) -3):
            right_diagonal_numbers = np.array([target_array[i, k], target_array[i+1, k+1], target_array[i+2, k+2], target_array[i+3, k+3]])
            right_diagonal_multiples.append(right_diagonal_numbers.prod())

    # 左斜下方向の積一覧
    left_diagonal_multiples = []
    for i in range(len(target_array) - 3):
        for k in range(len(target_array[i]) -3):
            left_diagonal_numbers = np.array([target_array[i, k+3], target_array[i+1, k+2], target_array[i+2, k+1], target_array[i+3, k]])
            left_diagonal_multiples.append(left_diagonal_numbers.prod())

    print(max(horizontal_multiples + vertical_multiples + right_diagonal_multiples + left_diagonal_multiples))  # answer 70600674


    # おまけとして、どこの積だったかを探る。
    print(max(horizontal_multiples))        # 48477312
    print(max(vertical_multiples))          # 51267216
    print(max(right_diagonal_multiples))    # 40304286
    print(max(left_diagonal_multiples))     # 70600674 → ここに答えが入ってる。

    print(left_diagonal_multiples.index(70600674))  # left_diagonal_multiplesの207番目の要素が答えだと分かる。
    row, column = divmod(207, 17)
    print(row+1, column+4)  # 13, 7となり、13行目7列目から左斜め下に4つの積(84, 94, 97, 87)
