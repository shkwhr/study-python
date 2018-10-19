# coding: utf-8

list_a = []
for a in range(10):
    list_a.append(a + 1)
print(list_a)

# リスト内包表記 1
list_b = list(map(lambda b: b + 1, range(10)))
print(list_b)

# リスト内包表記 2:
list_c = [c + 1 for c in range(10)]
print(list_c)

# この表記は違う
list_d = [map(lambda d: d + 1, range(10))]
print(list_d)  # map object

# 複雑なの
list_e = []
for e_1 in range(10):
    for e_2 in range(10):
        if e_1 == e_2:
            list_e.append(e_1 + 1)
print(list_e)

# 複雑なのリスト内包表記
list_f = [f_1 + 1 for f_1 in range(10) for f_2 in range(10) if f_1 == f_2]
print(list_f)
