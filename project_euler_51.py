# -*- coding: utf-8 -*-

'''
Problem51 「Prime digit replacements」

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
(数字の一部（必ずしも隣接する桁でなくてもよい）を同じ数字に置き換えることで、８つの素数ができる最小の素数を求めよ。)
'''

import time
from itertools import combinations
from functions import is_prime

def has_same_digit_number(num):
    if len(str(num)) != len(set(str(num))):
        return True
    else:
        return False

# 被っている数字のリストを生成
def generate_same_digit_number_list(num):
    str_num = str(num)
    return [int(number) for number in list(set(str_num)) if str_num.count(number) > 1]

# 指定した数字が何桁目にあるかのリストを生成
# 例:generate_same_digit_list(1315671, 1) は [0, 2, 6]を返す。
def generate_same_digit_list(num, same_digit_num):
    str_num = str(num)
    str_same_digit_num = str(same_digit_num)
    slice_at = 0
    same_digit_list = []
    while True:
        found_digit = str_num.find(str_same_digit_num, slice_at)
        if found_digit == -1:
            return same_digit_list
        else:
            same_digit_list.append(found_digit)
            slice_at = found_digit + 1

def check_replaced_numbers(num, number_of_replace_digit, replace_number, value_count=8):
    str_num = str(num)
    same_digit_list = generate_same_digit_list(num, replace_number)

    # 例えば122342で2を2ヶ所置換する時、置換場所のインデックスの選び方が[1, 2], [1, 5], [2, 5]の3通りあるので全て調べる
    for pair in combinations(same_digit_list, number_of_replace_digit):
        if (len(str_num)-1) in pair:
            continue
        # まずは置き換える箇所をXにした文字列を作成
        for slice_at in pair:
            str_num = str_num[:slice_at] + 'X' + str_num[slice_at+1:]
        # num自身が素数の場合にチェックするようにするので,countは1からスタートとする
        count = 1
        # replace_numberより大きい数字へしか置換しない。
        for i in range(replace_number+1, 10):
            if is_prime(int(str_num.replace('X', str(i)))):
                count += 1
        if count == value_count:
            return True
        else:
            pass
    return False

if __name__ == '__main__':
    # https://qiita.com/you1111/items/92bd776d6c40559dc88e によると、置き換える箇所の個数は3の倍数である必要があるとのこと。
    start = time.time()

    target = 3
    flag = False
    while True:
        if not is_prime(target):
            pass
        elif has_same_digit_number(target):
            same_digit_number_list = generate_same_digit_number_list(target)
            for same_digit_number in same_digit_number_list:
                # 8個あるためには、置換する数字は0, 1, 2のどれかでないといけない。
                if same_digit_number not in {0, 1, 2}:
                    pass
                else:
                    same_digit_number_count = str(target).count(str(same_digit_number))
                    if same_digit_number_count < 3:
                        pass
                    else:
                        for number_of_replace_digit in [number for number in range(1, same_digit_number_count + 1) if number % 3 == 0]:
                            if check_replaced_numbers(target, number_of_replace_digit, same_digit_number):
                                print(target)   # answer 121313
                                flag = True
                                break
                if flag == True:
                    break
        if flag == True:
            break
        else:
            target += 2

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.16749sec
