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
