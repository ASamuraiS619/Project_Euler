# -*- coding: utf-8 -*-

'''
Problem19 「日曜日の数え上げ」

次の情報が与えられている.
    ・1900年1月1日は月曜日である.
    ・9月, 4月, 6月, 11月は30日まであり, 2月を除く他の月は31日まである.
    ・2月は28日まであるが, うるう年のときは29日である.
    ・うるう年は西暦が4で割り切れる年に起こる. しかし, 西暦が400で割り切れず100で割り切れる年はうるう年でない.
20世紀（1901年1月1日から2000年12月31日）中に月の初めが日曜日になるのは何回あるか?
'''

import time

if __name__ == '__main__':
    start = time.time()

    date = { "year":1900,  "month":1, "days":0 }
    finish_year = 2001
    finish_month = 1
    sunday_count = 0

    while True:
        if date["year"] == finish_year and date["month"] == finish_month:
            break
        else:
            if date["days"] % 7 == 6 and date["year"] >= 1901:
                sunday_count += 1

            # daysを最初にずらす
            if date["month"] in [4, 6, 9, 11]:
                date["days"] += 30
            elif date["month"] in [1, 3, 5, 7, 8, 10, 12]:
                date["days"] += 31
            elif date["year"] % 400 == 0:
                date["days"] += 29
            elif date["year"] % 100 == 0:
                date["days"] += 28
            elif date["year"] % 4 == 0:
                date["days"] += 29
            else:
                date["days"] += 28

            #monthとyearをずらす
            if date["month"] == 12:
                date["year"] += 1
                date["month"] = 1
            else:
                date["month"] += 1

    print(sunday_count) # answer 171

    elapsed_time = time.time() - start
    print("elapsed_time:{}".format(round(elapsed_time, 5)) + "[sec]")   # 0.00072sec
