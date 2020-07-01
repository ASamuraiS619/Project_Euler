# -*- coding: utf-8 -*-

'''
Problem10 「素数の和」

10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.
200万以下の全ての素数の和を求めよ.
'''

import time

#エラトステネスの篩でnumber以下の素数を列挙
def primes_up_to(number):
    # 検査の上限値
    border_line = int(number ** 0.5)
    prime_numbers = [2]
    target_list = list(range(3, number + 1, 2))

    while True:
        mesh_number = min(target_list)
        # 検査がborder_lineを超えると残りは全て素数なのでprime_numbersへ。
        if mesh_number > border_line:
            prime_numbers.extend(target_list)
            break
        prime_numbers.append(mesh_number)

        # mesh_numberで篩いにかける。割り切れなかったものを次の候補へ
        tmp_target_list = []
        for i in target_list:
            if i % mesh_number != 0:
                tmp_target_list.append(i)
        target_list = tmp_target_list

    return prime_numbers


if __name__ == '__main__':
    start = time.time()
    print(sum(primes_up_to(2000000)))   # answer 142913828922
    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 3)) + "[sec]")   # 5.842sec
