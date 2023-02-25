# Problem link: https://leetcode.com/problems/baseball-game/description/

# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations,
# where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x: Record a new score of x.
# '+': Record a new score that is the sum of the previous two scores.
# 'D': Record a new score that is the double of the previous score.
# 'C': Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        arr = []
        sum = 0
        for x in operations:
            if (x.startswith("-") or x.isdigit()):
                x = int(x)
                arr.append(x)
                sum += x
            elif (x == 'C'):
                sum -= arr.pop()
            elif (x == 'D'):
                arr.append(arr[len(arr) - 1] * 2)
                sum += arr[len(arr) - 1]
            elif (x == '+'):
                arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])
                sum += arr[len(arr) - 1]
        return sum