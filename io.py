# coding: utf-8
# 単行処理
print("Please input your name: ", end='')
input_name = input().rstrip()
print("hello " + input_name)

# 複数行処理
print('Please input yourself: ')
yourself = []
import sys
for line in sys.stdin.readlines():
    yourself.append(line.rstrip())
print(yourself)