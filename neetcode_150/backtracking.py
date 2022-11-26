class Solution:
    def subsets(self, nums):
        """
        [1,2,3]
        len(ind) --> 3
        
        
        ([],0)
        ([1],1)
        ([1,2],2)
        ([1,2,3],3)
        res = [[1,2,3]]
        
        ([1,2],3) 
        res = [[1,2,3],[1,2]]
        
        
        """
        res = []

        subset = []

        def dfs(subset,ind):
            if ind == len(nums):
                # add solution
                res.append(subset)
                return
                
            # do add
            dfs(subset+[nums[ind]], ind+1)

            # don't add
            dfs(subset,ind+1)

        dfs(subset,0)

        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        from prior power set problem I recall that the trick was to treat this as a tree and at each (level? node?)
        the choice is either do include this value or do not

        so solution feels like a dfs approach

        ind = 0
        solution = []

        [1], ind = 1
        [1,2], ind = 2
        [1,2,2], ind = 3

        output = [[], [1,2,2]]

        [1,2] ind = 2
        time complexity: O(N*2^^N)
        space complexity: O(N)
        """

        output = []
        current_solution = []

        def dfs(current_solution,ind):
            nonlocal output
            # stopping criteria check
            if ind == len(nums):
                if sorted(current_solution) not in output:
                    output.append(sorted(current_solution))
                return
            else:
                dfs(current_solution + [nums[ind]], ind + 1)
                dfs(current_solution, ind + 1)

        dfs(current_solution,0)

        return output
