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

    def canJump(self, nums):
        """
        feels like a potential dfs tree type of problem as this is about simulations

        root
        2
        children = [1,2]

        if 1 --> 3: children = [1,2,3]
        if 1, etc.

        time complexity = O(2^N) cloudy here, but it's definitely something exponential
        space compelxity = O(N) ish?
        """
        
        explored_dict = {}

        if len(nums) == 1:
            return True

        def dfs(ind):
            nonlocal output, nums
#             print(f'at {ind}')
            
            # is if out of bounds?
            if ind >= len(nums) - 1:
                output = True
                return True
            else:
                val = nums[ind]
            
            # stopping criteria?
            if val == 0:
                return False
            
            elif val > len(nums[ind:]):
                output = True
                return True
            
            elif ind in explored_dict:
                return False
            
            # keep searching
            priority = range(1,val+1)[::-1]
#             import pdb;pdb.set_trace()
            for c in priority[:100]:
                jmp = ind + c
                if not dfs(jmp): # new index we are jumping to
                    explored_dict[jmp] = 1
            

        output = False
        dfs(0)
        return output 
