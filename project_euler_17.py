# -*- coding: utf-8 -*-

'''
Problem17 「数字の文字数」

1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.
では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.

注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は 23 文字, 115 (one hundred and fifteen) は20文字と数える. なお, "and" を使用するのは英国の慣習.
'''

basic_numbers = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_place_numbers = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

count_up_to_ninety_nine = 0
# まずは19までを数える
for number in (basic_numbers + ten_to_nineteen):
    count_up_to_ninety_nine += len(number)

# 残りの99までを数える
for tens_place_number in tens_place_numbers:
    for ones_place_number in basic_numbers:
        count_up_to_ninety_nine += len(tens_place_number + ones_place_number)

total_count = count_up_to_ninety_nine


for hundreds_place_number in basic_numbers[1:]:
    # '○○ hundred'ピッタリは別で足しておく。
    total_count += len(hundreds_place_number + 'hundred')
    # 結局増えるところは'○○ hundred and'だけなのでそれを99回分count_up_to_ninety_nineに加えて足す。
    total_count += len(hundreds_place_number + 'hundred' + 'and') * 99 + count_up_to_ninety_nine

total_count += len('one' + 'thousand')

print(total_count)  # answer 21124
