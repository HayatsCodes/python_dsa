# static arrays are fixed size
# reading and writing values to a static array that has space is O(1)
# removing/writing to the end of an array is O(1)
# removing/inserting to any other spot in the array is inefficient and it's O(n)

# EXAMPLE:

# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    if length > 0:
        # Overwrite last element with some default value.
        # We would also the length to decreased by 1.
        arr[length - 1] = 0

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    
    # Insert at i
    arr[i] = n

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]

def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])


# dynamic arrays size varies
# reading and writing to it has an amortized time complexity 
# (i.e average time it takes) of O(1) since it creates new array
# any time there's no space for more values
# Thus, dynamic arrays has the same time complexity as static arrays


# Python arrays are dynamic by default, but this is an example of resizing.
class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # Array of capacity = 2

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity 
        
        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr
        
    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1
    
    # Get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.arr[i]
        # Here we would throw an out of bounds exception

    # Insert n at i-th index
    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return
        # Here we would throw an out of bounds exception       

    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()


