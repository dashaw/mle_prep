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

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        s = "applepenapple", 
        wordDict = ["apple","pen"]

        - is word in s
        - if yes, essentially remove that part of s
        -
        """
        len_s = len(s)
        cnd = False
        memo = {}

        def dfs(ind):
            nonlocal cnd
            if ind == len_s:
                cnd = True

            if cnd == True:
                return

            if ind in memo.keys():
                return

            else:
                for w in wordDict:
                    len_w = len(w)
                    candidate_s = s[ind:ind+len_w]
                    if ind + len_w <= len_s and candidate_s == w:
                        dfs(ind+len_w)

                if cnd == False:
                    memo[ind] = False
                    
                

        
        # search
        dfs(0)

        return cnd

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            min_coins = math.inf
            for c in coins:
                new_amount = amount - c
                if new_amount >= 0:
                    min_coins = min(min_coins, dfs(new_amount) + 1)

            memo[amount] = min_coins
            return min_coins

        res = dfs(amount)
        return res if res != math.inf else -1

    def numDecodings(self, s: str) -> int:
        """
	https://leetcode.com/problems/decode-ways
        ### Examples
        s = "226", output = 3
        note: do not need to output the solutions, just the number

        #### option 1
        solution space:
        -> 2 -> 2 -> 6 (end)
             -> 26 (end)
        -> 22 
            -> 6 (end)

        can use dfs to determine eligible solutions

        #### option 2
        from left to right
        dp[0] = 1
        [2]
        dp[1] = 1
        [22]
        
        """
        # base case
        dp = [0]*(len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2,len(dp)):
            if s[i-1] != "0":
                dp[i] = dp[i-1]

            two_digits = s[i-2:i]
            if int(two_digits) >= 10 and int(two_digits) <= 26:
                dp[i] += dp[i-2]


        return dp[-1]
