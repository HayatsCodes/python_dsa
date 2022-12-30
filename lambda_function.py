my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))

new_list = [5, 4, 3]
print(list(map(lambda item: item**2, new_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)