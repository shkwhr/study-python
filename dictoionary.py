# coding: utf-8

item_dic = {'醤油': 100, '砂糖': 80, '胡椒': 70}
item_dic2 = sorted(item_dic, reverse=True)

for (name, price) in item_dic.items():
    print(name + 'は' + str(price) + '円です')

print('Price Only')
for name in item_dic:
    print(str(item_dic[name]) + '円')