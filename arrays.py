# static arrays are fixed size
# reading and writing values to an array is O(1)
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
# its has an amortized time complexity of O(1) (i.e average time it takes)