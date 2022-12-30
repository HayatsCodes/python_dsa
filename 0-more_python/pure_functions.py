def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list
# print is a side effect so it violates pure 
# function 2nd rule
# print(multiply_by2([1,2,3]))

