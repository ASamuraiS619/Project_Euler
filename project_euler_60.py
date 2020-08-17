# -*- coding: utf-8 -*-

'''
Problem60 「Prime pair sets」

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
(互いをどのような順で結合しても素数になる5つの数字の組の合計の最小値を求めよ。)
'''

import time
from itertools import product, combinations
from functions import is_prime

def is_the_prime_pair_sets(primes, prime_pair_combination_dict):
    for index, prime1 in enumerate(primes):
        for prime2 in primes[index+1:]:
            if prime2 not in prime_pair_combination_dict[prime1]:
                return False
    return True

def is_the_prime_pair(prime1, prime2):
    str_prime1 = str(prime1)
    str_prime2 = str(prime2)
    if is_prime(int(str_prime1 + str_prime2)) and is_prime(int(str_prime2 + str_prime1)):
        return True
    else:
        return False

if __name__ == '__main__':
    start = time.time()

    # ある素数について、全2通りの結合した数字が素数である自分より大きい素数の集合を辞書にする。
    # 例えば、3と7は37, 73ともに素数なので{3: {7, …}, …}となっている。
    # これを使ってis_the_prime_pair_setsについて、全組み合わせが条件を満たしているか確認すれば二度手間にならず処理が短縮できる。
    prime_pair_combination_dict = {}
    primes, targets, answer_sets = [], [], []
    num = 3
    minimum_sum = None
    while True:
        if is_prime(num):
            primes.append(num)
            prime_pair_combination_dict[num] = set()
            # targetsを初期化
            targets = []
            for prime in primes[:-1]:
                if is_the_prime_pair(prime, num):
                    prime_pair_combination_dict[prime].add(num)
                    targets.append(prime)
            # targetsに4つ以上数字が無ければそもそも5つの数字の組にならない。
            if len(targets) >= 4:
                print(num)
                # targetsについて、全組み合わせを試す。
                # 条件を満たし、かつ、合計が最小であれば答えとなる。
                for prime_set in combinations(targets, 4):
                    # prime_setの中身はnumとは条件を満たしているので、残りの数字について全組み合わせで条件を満たしているか確認すればOK。
                    if is_the_prime_pair_sets(prime_set, prime_pair_combination_dict):
                        _sum = sum(prime_set) + num
                        if minimum_sum is None or _sum < minimum_sum:
                            answer_sets = prime_set
                            minimum_sum = _sum
        if answer_sets == []:
            num += 2
        else:
            # print(answer_sets, num) # (13, 5197, 5701, 6733) と 8389
            print(minimum_sum) # answer 26033
            break

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 13.75395sec
