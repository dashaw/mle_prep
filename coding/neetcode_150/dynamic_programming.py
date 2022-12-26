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


