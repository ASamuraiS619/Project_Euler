# -*- coding: utf-8 -*-

'''
Problem67 「最大経路の和 その2」

以下の三角形の頂点から下の行の隣接する数字を通って下まで移動するとき, その数値の和の最大値は23になる.

             [3]
          [7]    4
         2   [4]   6
       8   5    [9]  3
この例では 3 + 7 + 4 + 9 = 23.

100列の三角形を含んでいる15Kのテキストファイル triangle.txt (右クリックして, 『名前をつけてリンク先を保存』)の上から下まで最大合計を見つけよ.

注：これは, Problem 18のずっと難しいバージョンです.
全部で299 通りの組み合わせがあるので, この問題を解決するためにすべてのルートをためすことは可能でありません！
あなたが毎秒1兆本の(1012)ルートをチェックすることができたとしても, 全てをチェックするために200億年以上かかるでしょう.
解決するための効率的なアルゴリズムがあります. ;o)


'''

import time

if __name__ == '__main__':
    start = time.time()

    with open('p067_triangle.txt') as f:
        s = f.read()
        pyramid_str = s
    pyramid = pyramid_str.split('\n')
    # 各行について、スペースで区切りつつ、後の計算のために前後に'0'を入れる。
    pyramid = list(map(lambda x: ['0'] + x.split(' ') + ['0'], pyramid))

    # 下の隣接する2項を比べて大きい方を足し、自分自身をそれとの和に置き換える。
    # これを下から順に行い上まで繰り返せば、求める最大の和が一番上に出てくる。

    for i in range(len(pyramid) - 3, -1, -1):
        for k in range(1, len(pyramid[i]) -1):
            pyramid[i][k] = int(pyramid[i][k]) + max(int(pyramid[i+1][k]), int(pyramid[i+1][k+1]))

    print(pyramid[0][1])    # answer 7273(最小は2768)

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00535sec
