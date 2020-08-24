# -*- coding: utf-8 -*-

'''
Problem68 「Magic 5-gon ring」

下に示す図のようなものを"magic" 3-gon ringという. これは1～6の数字を当てはめて, 各列の数字の和が9となっている. これを例として説明する.

外側のノードのうち一番小さいものの付いた列(例では4,3,2)から時計回りに回ってそれぞれ列の数字を3つ連ねて説明する. 例えば例のものは4,3,2; 6,2,1; 5,1,3という組で説明することができる.

1～6の数字を当てはめて, 各列の数字の和が等しくなるものは次の8通りある.

合計	組
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
この組の各数字を連結して, 9桁の数字で表すことができる. 例えば, 上の図のものは4,3,2; 6,2,1; 5,1,3であるので432621513である.

さて, 下の図に1～10の数字を当てはめ, 各列の数字の和が等しくなる"magic" 5-gon ringを作って, それを表す16桁または17桁の数字のうち, 16桁のものの最大の数字を答えよ.

(注, 3つの場合の例を見ても分かる通り, 列の始まりの数字を比べた時一番小さい数字で始まる列から時計回りに繋げるという条件のもとで文字列を生成する必要があります. この条件下で最大となる数字を答えてください. )

※図はhttps://projecteuler.net/problem=68を参照。
'''

import time
from itertools import combinations, permutations

def produce_magic_ring(outside_number_and_inside_list={}):
    outside_number_and_inside_list_orderdict = list(outside_number_and_inside_list.items())
    magic_ring = {}
    for i in range(2):
        last_inside_number = outside_number_and_inside_list_orderdict[0][1][i]
        if last_inside_number not in outside_number_and_inside_list_orderdict[1][1]:
            continue
        for index in range(len(outside_number_and_inside_list_orderdict)):
            # for文のindexのままだと後半で+1, +2をした際にout of rangeとなってしまうので、マイナス表記に変換
            index -= len(outside_number_and_inside_list_orderdict)
            next_inside_number_list = outside_number_and_inside_list_orderdict[index + 1][1]
            if last_inside_number in next_inside_number_list and [num for num in next_inside_number_list if num != last_inside_number][0] in outside_number_and_inside_list_orderdict[index + 2][1]:
                magic_ring[outside_number_and_inside_list_orderdict[index][0]] = [[num for num in outside_number_and_inside_list_orderdict[index][1] if num != last_inside_number][0], last_inside_number]
                last_inside_number = [num for num in next_inside_number_list if num != last_inside_number][0]
            else:
                return None
        return magic_ring

if __name__ == '__main__':
    start = time.time()

    GON_NUMBER = 5
    ALL_NUMBERS = range(1, GON_NUMBER * 2 + 1)

    answer = 0
    for inside_numbers in combinations(ALL_NUMBERS, GON_NUMBER):
        inside_numbers_origin = list(inside_numbers)
        all_length_total = (sum(ALL_NUMBERS) + sum(inside_numbers))
        if all_length_total % GON_NUMBER != 0:
            continue
        outside_numbers_combination = list(set(ALL_NUMBERS) ^ set(inside_numbers))
        length_total = all_length_total // GON_NUMBER
        # inside_numbersは全2回ずつ出てくる。
        for outside_numbers in permutations(outside_numbers_combination):
            # 列の始まりの数字を比べた時一番小さい数字で始まる列から時計回りに繋げるという条件があるので最初が最小で無いものは除外
            if outside_numbers[0] != min(outside_numbers):
                continue
            inside_numbers = inside_numbers_origin[:] + inside_numbers_origin[:]
            outside_number_and_inside_list = {}
            for outside_number in outside_numbers:
                for inside_number1 in inside_numbers:
                    inside_number2 = length_total - outside_number - inside_number1
                    if inside_number2 != inside_number1 and inside_number2 in inside_numbers:
                        outside_number_and_inside_list[outside_number] = [inside_number1, inside_number2]
                        inside_numbers.remove(inside_number1)
                        inside_numbers.remove(inside_number2)
                        break
                    else:
                        pass
            if len(outside_number_and_inside_list.keys()) != GON_NUMBER:
                continue
            magic_ring = produce_magic_ring(outside_number_and_inside_list)
            if magic_ring is not None:
                formed_string = ''
                for outside_number, inside_numbers in magic_ring.items():
                    formed_string += str(outside_number)
                    for inside_number in inside_numbers:
                        formed_string += str(inside_number)
                # 16桁 or 17桁になるが、16桁の中で最大を探すようにと指定がある。
                if len(formed_string) == 16 and int(formed_string) > answer:
                    answer = int(formed_string)

    print(answer)   # answer 6531031914842725

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.01269sec
