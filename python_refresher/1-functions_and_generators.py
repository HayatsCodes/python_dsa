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


""" Exercise 1... """
print('Exercise 1...')
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

print()

""" Exercise 2... """
print('Exercise 2...')
print('-----------------')
print()


correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(square):
    """ Checks for valid sudoku solution.

        Return:
            True if it's valid, else false
    """
    # loop through the rows in square
    # create a check_column variable on each iteration to check for 1 - n numbers
    # after finding the number remove it from check_column
    # else return false
    # loop through 0 to the length of square - 1 using n
    # create a check_row simmilar to check_column
    # if row[n] is not in check_row
    #   return false
    # return true

    for rows in square:
        check_column = list(range(1, len(square) + 1))
        for i in rows:
            if (i not in check_column):
                return False
            check_column.remove(i)
    for n in (range(len(square) - 1)):
        check_row = list(list(range(1, len(square) + 1)))
        for row in square:
            if row[n] not in check_row:
                return False
            check_row.remove(row[n])
    return True




    
    
print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False
