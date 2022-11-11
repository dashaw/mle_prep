"""
storing neetcode 150 solutions for Arrays & Hashing problems
"""
class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/

        Args:
          nums (List[int]): array of integers

        Returns:
           True if duplicates
        """
        num_dict = {}
        for i in nums:
            if i in num_dict.keys():
                return True
            else:
                num_dict[i] = 'found'

        return False
