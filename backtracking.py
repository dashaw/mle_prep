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
