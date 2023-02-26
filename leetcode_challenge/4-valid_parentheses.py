# Problem link: https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_dict = {'(': ')', '{': '}', '[': ']'}
        a_stack = []

        if len(s) == 1:
            return False

        for x in s:
            if x in s_dict:
                a_stack.append(x);
            elif x in s_dict.values():
                if len(a_stack) == 0:
                    return False
                if x == s_dict[a_stack[- 1]]:
                    a_stack.pop()
                else:
                    return False
        if len(a_stack) >= 1:
            return False
        return True