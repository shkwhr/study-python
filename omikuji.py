# coding: utf-8
import random

# number = random.random()
number = random.randint(1, 10)

if number == 1:
    print('大吉')
elif number <= 2:
    print('吉')
elif number <= 4:
    print('中吉')
elif number <= 6:
    print('小吉')
elif number <= 8:
    print('凶')
else:
    print('大凶')
