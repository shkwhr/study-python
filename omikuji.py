# coding: utf-8
import random

def output_all():
    print('出るもの ', end='')
    for (i, text) in enumerate(result):
        print(str(i) + ': ' + text + ' ', end='')
    print()

def execute_omikuji():
    print('結果: ', end='')
    if number == 1:
        print(result[0])
    elif number <= 2:
        print(result[1])
    elif number <= 4:
        print(result[2])
    elif number <= 6:
        print(result[3])
    elif number <= 8:
        print(result[4])
    else:
        print(result[5])


# number = random.random()
number = random.randint(1, 10)
# result = ['大吉', '吉', '中吉', '末吉', '凶', '大凶']
result_str = '大吉,吉,中吉,末吉,凶,大凶'
result = result_str.split(',')
result.append('超凶')   # 追加
# result.pop(6)           # 削除
# result.remove('超凶)
del result[6]
result[3] = '小吉'      # 変更

output_all()

execute_omikuji()

