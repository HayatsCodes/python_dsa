class  Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1
    
    def getName(self):
        return self.person_name
    

bob = Person('Bob', 32)
print(bob.getName())
bob.birthday()
print(bob.person_age)






"""
Exercise

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]



nums = [3,3]
target = 6

my_sum = Solution()
index_list = my_sum.twoSum(nums, target)
print(index_list)