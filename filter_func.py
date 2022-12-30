def check_odd(item):
    return item % 2 != 0

my_list =[1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(filter(check_odd, my_list))
print(new_list)