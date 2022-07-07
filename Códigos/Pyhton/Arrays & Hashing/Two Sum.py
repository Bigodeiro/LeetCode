#https://leetcode.com/problems/two-sum/
#?Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#! Versão extramente devagar, porém eficiente em memória
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]