def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list
# prit is a side effect so it violates pure function rule
print(multiply_by2([1,2,3]))