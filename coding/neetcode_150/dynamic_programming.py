class Solution:
    def climbStairs(self, n: int) -> int:
        """
        bottom-up dp
        solve the base case and one more, then iterate backward using this result and updating
        """
        # initialize vars
        one, two = 1, 1

        for i  in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        start from back
        cost = end cost
        [1,100,1,1,1,100,1,1,100,1]
                             1+min(),100,1
        """
        min_cost = [0]*len(cost)
        min_cost[-1] = cost[-1]
        min_cost[-2] = cost[-2]

        for i in range(len(cost) - 2)[::-1]:
            min_cost[i] = min(min_cost[i+1],min_cost[i+2]) + cost[i]
        
        return min(min_cost[0], min_cost[1])

    def rob(self, nums: List[int]) -> int:
        """
        [2,7,9,3,1]
        [2,7,11,11]

        left = 7
        right = 11
        we iterate left --> right and keep a cumulative(ish) result based on our constraints
        at each iteration we look to the left, apply our constraint, and make a decision that maximizes value to that point
        """
        # edge case
        if len(nums) == 1:
            return nums[0]

        # vars 
        left = nums[0]
        right = nums[1]

        if len(nums) == 2:
            return max(left, right)

        # happy-case logic
        for i in range(2,len(nums)):
            if left + nums[i] > right:
                temp = max(left, right)
                right = left + nums[i]
                left = temp
            else:
                # do something else
                left = right

        return right
