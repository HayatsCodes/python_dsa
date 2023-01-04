""" Iteration With Loops """
print('Iteration With Loops...')
print('------------------------')
print()

my_list = [0, 1, 2, 3, 4, 5]

for item in my_list:
    print('The value in my_list is: ', str(item))

for i, value in enumerate(my_list):
    print('The index value: is, ', str(i), '. The value at i is: ', str(value))

i = 0
while (i < 10):
    print(i, end=", ")
    i += 1
print()

my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])

for key, value in my_dict.items():
    print(key + ': ' + value)
print()

""" Conditional Statements """
print('Conditional Statements...')
print('------------------------')
print()

num = 5
if num < 5:
    print('The number is smaller than 5.')
elif num == 5:
    print('The number equals 5.')
else:
    print('The number is greater than 5.')

print()

""" Exercise 1 """
print('Exercise 1')
print('------------------------')
print()


def smallest_positive(in_list):
    """
    TODO: Define a control structure that finds the smallest positive
          number in in_list and returns the correct smallest number.
    """
    # create a variable isSmallest
    # loop through the numbers and check if it's smaller than isSmallest
    # and is not less than 0
    # if yes set ismallest to the number
    # return isSmalest

    is_smallest = in_list[0]
    for i in in_list:
        if (i <= is_smallest and i >= 0):
            is_smallest = i
    return is_smallest
    # Test cases


print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
print()

""" Exercise 2 """
print('Exercise 2...')
print('------------------------')
print()


# This exercise uses a data structure that stores course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': {'cs101': {'name': 'Building a Search Engine',
                             'teacher': 'Dave',
                             'assistant': 'Peter C.'},
                   'cs373': {'name': 'Programming a Robotic Car',
                             'teacher': 'Sebastian',
                             'assistant': 'Andy'}},
    'fall2020': {'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                             'teacher': 'Dorina'},
                   'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                             'teacher': 'Jasper'},
                   }
}


def when_offered(courses, course):
    # TODO: Fill out the function here.

    # create an empty course_semester list
    # loop through the courses dictionary
    # check for the course
    # if it exists in the semester
    # append the semester to course_semester

    # course_semester = [[k for key in courses[k]] for k in courses if (course == key)]
    course_semester = []
    for k in courses:
        for key in courses[k]:
            if (course == key):
                course_semester.append(k)
    # TODO: Return list of semesters here.
    # return the course_semester
    return (course_semester)


print(when_offered(courses, 'cs101'))
# Correct result:
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result:
# []
