class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            print(f'a = {a}')
            print(f'i = {i}')
            a ^= i
            print(f'a = {a}')
            print('--------')
        return a
