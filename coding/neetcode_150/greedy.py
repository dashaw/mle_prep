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

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        ### Examples
        https://leetcode.com/problems/gas-station
        we want to find the starting point that allows us to get around to all gas stations
        the solution space is any index in gas array or -1

        #### 1
        gas = [2,3,4], cost = [3,4,3]
        if we start at index 0 we see that gas[0] < cost[0] so we can't even go to next station
        if we start at index 1 we see that gas[1] < cost[1] so we can't even go to next station
        so let's try the final index. gas[2] > cost[2] and gas = 4-3 = 1
            -> at ind[0]: gas = 1 + 2 = 3 which is == cost[0] -> gas = 0
            -> at ind[1] gas = 0+3 which is less than cost[1] so can't make it around
            -> output -1

        #### 2
        gas = [2,1,0,3,2], cost = [1,0,2,0,1]
        start = ind[0]
            * [0]: gas = 2 - 1 = 1
            * [1]: gas = 1+1 - 0 = 2
            * [2]: gas = 2 + 0 - 2 = 0
            * [3]: gas = 3 + 0 - 0 = 3
            * [4]: gas = 3 + 2 - 1 = 4
            * [0]: gas = 4+2-1 pass

        ### Approach
        * iterate through all indices, run the simulation and see if pass, if yes then output index, else continue
        * if go through all indices then we haven't found a solution and output -1
        * time = O(n^2)
        * space = O(1)

        ### Examples
        gas = [2,3,4], cost = [3,4,3]
        len_gas = 3
        ind = 0
        * tank_cnt = 0 -> 2
        * 
        ind = 1

        ind = 2
        * tank_cnt = 0 -> 4
        * 4 < 3 -> false
        """

        # init vars
        len_gas = len(gas)
        solution_dict = {}
        sum_gas = 0
        sum_cost = 0
        diff_array = []

        # take sums to see if this even works
        for i in range(len_gas):
            sum_gas += gas[i]
            sum_cost += cost[i]
            diff_array.append(gas[i] - cost[i])

        # is there a solution?
        if sum_cost > sum_gas:
            return -1

        # yes, so iterate
        total = 0
        res = 0
        for i in range(len_gas):
            total += diff_array[i]

            if total < 0:
                total = 0
                res = i + 1

        return res
