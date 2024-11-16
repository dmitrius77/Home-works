from operator import index

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
w = len(my_list)
q = my_list[index]
while q >= 0 and index < w:
    q = my_list[index]
    index = index + 1
    if q == 0:
        continue
    if q < 0:
        break
    print(q)