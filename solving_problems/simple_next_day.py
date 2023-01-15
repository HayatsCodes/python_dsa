###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE

    # if day not equal 30, increment day by 1,
    # else if day == 30 and year not equal 12, day = 1, month += 1
    # else if day == 30 and year == 12, day = 1, month += 1, year += 1
    if day != 30:
        day += 1
    elif day == 30 and month != 12:
        day = 1
        month += 1
    else:
       day = 1
       month = 1
       year += 1
    return (year, month, day)


print(nextDay(1999, 12, 30));
print(nextDay(2013, 1, 30))
print(nextDay(2012, 12, 30))
