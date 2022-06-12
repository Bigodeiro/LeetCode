#https://leetcode.com/problems/contains-duplicate/
#?Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


#* Hashset: usando hashset o algoritimo será muito mais eficiente

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()

        for n in nums:

            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

#*Brute force: comparar cada elemento com o array inteiro

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = 0
        j = 0

        while i < len(nums):
            j = i + 1

            while (j) < len(nums):

                if nums[j] == nums[i]:
                    return True

                j += 1
            i += 1
        return False

#*Sorting: Organizar o array e comparar os elementos adjacentes

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:

        i = 1
        nums.sort()

        while i < len(nums):
            if nums[i] == nums[i-1]:
                return True
            i += 1
        return False