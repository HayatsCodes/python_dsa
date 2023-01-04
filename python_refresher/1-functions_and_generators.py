""" Python Functions """
print('Python Functions')
print('-----------------')
print()


def sum(a, b):
    return a+b

def list_sort(my_list):
    my_list.sort()
    return len(my_list), my_list

print(list_sort([4, 2, 8, 1]))
print()


""" Python Generators """
print('Python Generators')
print('-----------------')
print()

def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()
for i in range(5):
    print(next(my_gen))

print("Do Something")
print("Do Something again!")

for i in range(100):
    print(next(my_gen))

print()


""" Exercis 1... """
print('Exercis 1...')
print('-----------------')
print()

def prod(a,b):
    # TODO change output to the product of a and b
    output =  a * b
    return output

def fact_gen():
    i = 1
    n = i
    while True: 
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120




