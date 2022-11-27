class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        seems we could do this with a sliding window?

        time complexity = O(N)
        space = O(1)
        """
        max_value = -10**4
        curr_sum = 0
        len_nums = len(nums)
        left_pointer = 0
        right_pointer = 1

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_value = max(curr_sum, max_value)
            
        return max_value
