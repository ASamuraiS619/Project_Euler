# -*- coding: utf-8 -*-

'''
Problem54 「Combinatoric selections」

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	    Player 2	 	Winner
1	 	5H 5C 6S 7S KD 	    2C 3S 8S 8D TD
        Pair of Fives       Pair of Eights      Player 2

2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH
        Highest card Ace    Highest card Queen  Player 1

3	 	2D 9C AS AH AC 	    3D 6D 7D TD QD
        Three Aces          Flush with Diamonds Player 2

4	 	4D 6S 9H QH QC  	3D 6D 7H QD QS
        Pair of Queens      Pair of Queens      Player 1
        Highest card Nine   Highest card Seven

5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        Full House          Full House          Player 1
        With Three Fours    with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
(poker.txtで示されるポーカーの手の組み合わせについて、player1が勝っているのはいくつ?)
'''

import time

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val][0]

# Aceを14として扱うこととする。
def numbers_and_marks(hand):
    numbers, marks_set = [], set()
    for card in hand:
        marks_set.add(card[1])
        number_str = card[0]
        special_numbers = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        if number_str in special_numbers.keys():
            numbers.append(special_numbers[number_str])
        else:
            numbers.append(int(number_str))
    return sorted(numbers, reverse=True), marks_set

def pair_status(hand_numbers):
    numbers_set = set(hand_numbers)
    if len(numbers_set) == 5:
        return {num: 1 for num in hand_numbers}
    pairs = {num: 0 for num in list(numbers_set)}
    for number in hand_numbers:
        pairs[number] += 1
    return pairs

def is_straight(hand_numbers):
    if hand_numbers[0] - hand_numbers[-1] == 4:
        return True
    else:
        return False

def is_flash(hand_marks_set):
    if len(hand_marks_set) == 1:
        return True
    else:
        return False

"""
High Card: 0
One Pair: 1
Two Pairs: 2
Three of a Kind: 3
Straight: 4
Flush: 5
Full House: 6
Four of a Kind: 7
Straight Flush: 8
Royal Flush: 9
の様に役番号をつける。
"""

def check_score(hand_numbers, hand_marks_set):
    pair_combination = tuple(sorted(pair_status(hand_numbers).values(), reverse=True))
    # まずはペアー系の役
    pair_kind_scores = {(4, 1): 7, (3, 2): 6, (3, 1, 1): 3, (2, 2, 1): 2, (2, 1, 1, 1): 1}
    if pair_combination != (1, 1, 1, 1, 1):
        return pair_kind_scores[pair_combination]
    # ストレート系の役、フラッシュ
    else:
        # ロイヤルストレートフラシュ
        if hand_numbers == [14, 13, 12, 11, 10] and is_flash(hand_marks_set):
            return 9
        # ストレートフラッシュ
        elif is_straight(hand_numbers) and is_flash(hand_marks_set):
            return 8
        # ストレート
        elif is_straight(hand_numbers):
            return 4
        # フラッシュ
        elif is_flash(hand_marks_set):
            return 5
        # ハイカード
        else:
            return 0

# 役が引き分けで、数字の大小で勝敗を決める際に、判定に使う数字リストを順に見て勝敗を判定
# 以降、player1に関連するものはo_, player2に関連するものはt_を頭につける
def check_winning_through_numbers(o_numbers, t_numbers):
    for i in range(len(o_numbers)):
        if o_numbers[i] == t_numbers[i]:
            continue
        else:
            return o_numbers[i] > t_numbers[i]

def judge_if_player_one_wins(o_numbers, t_numbers, o_marks_set, t_marks_set):
    o_score = check_score(o_numbers, o_marks_set)
    t_score = check_score(t_numbers, t_marks_set)

    if o_score != t_score:
        return o_score > t_score
    # 役では引き分けの場合、数字で判定
    else:
        o_pair_status = pair_status(o_numbers)
        t_pair_status = pair_status(t_numbers)
        # ストレート系は最大値で判定可能
        if o_score in {4, 8, 9}:
            return o_numbers.max() > t_numbers.max()
        # フォーカードは4枚揃っている数字、フルハウス・スリーカードは3枚揃っている数字で判定可能
        elif o_score == 7:
            return get_keys_from_value(o_pair_status, 4) > get_keys_from_value(t_pair_status, 4)
        elif o_score in {6, 3}:
            return get_keys_from_value(o_pair_status, 3) > get_keys_from_value(t_pair_status, 3)
        # フラッシュ、ハイカードは大きい順に見ていって先に大きい数字が出たほうが勝ち
        elif o_score in {0, 5}:
            return check_winning_through_numbers(o_numbers, t_numbers)
        # ワンペアはまずはペアとなっている数字の大小を比べ、それで決着がつかない場合は残りの数字の大小を順に見る。
        elif o_score == 1:
            o_score_number = get_keys_from_value(o_pair_status, 2)
            t_score_number = get_keys_from_value(t_pair_status, 2)
            if o_score_number != t_score_number:
                return o_score_number > t_score_number
            else:
                o_numbers = list(set(o_numbers))
                o_numbers.remove(o_score_number)
                o_numbers = sorted(o_numbers, reverse=True)
                t_numbers = list(set(t_numbers))
                t_numbers.remove(t_score_number)
                t_numbers = sorted(t_numbers, reverse=True)
                return check_winning_through_numbers(o_numbers, t_numbers)
        # 最後に2ペアはペアとなっている数字の大小を順に見て、それで決着がつかない場合は最後の1枚の大小で判定。
        else:
            o_numbers = [k for k, v in o_pair_status if v == 2]
            t_numbers = [k for k, v in o_pair_status if v == 2]
            if o_numbers != t_numbers:
                return check_winning_through_numbers(o_numbers, t_numbers)
            else:
                return get_keys_from_value(o_pair_status, 1) > get_keys_from_value(t_pair_status, 1)



if __name__ == '__main__':
    start = time.time()

    count = 0
    with open('p054_poker.txt') as f:
        f = f.read().splitlines()
        for hand in f:
            hand = hand.split(' ')
            o_hand = hand[:5]
            t_hand = hand[5:]
            o_numbers, o_marks_set = numbers_and_marks(o_hand)
            t_numbers, t_marks_set = numbers_and_marks(t_hand)
            print(o_hand, t_hand)
            print(judge_if_player_one_wins(o_numbers, t_numbers, o_marks_set, t_marks_set))
            if judge_if_player_one_wins(o_numbers, t_numbers, o_marks_set, t_marks_set):
                count += 1

    print(count)    # answer 376

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.05755sec

