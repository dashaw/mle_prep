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

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        dfs
        each node you can add one from candidates
        if val > target, stop dfs
        if val == target, add to output if sorted(soln) not already

        time complexity:
        O(N^(T/M)) T/M essentially trying to swag on avg how much the trees will grow out

        space complexity: O(T/M) T/M recursive calls

        """

        output = []
        candidates = sorted(candidates) # O(log n)
        explored_dict = {}

        def dfs(soln, candidates):
            soln_sum = sum(soln)
            explored_dict[str(sorted(soln))] = 1

            if soln_sum == target and sorted(soln) not in output:
                # potentially add to output
                # sorted is O(logn)
                output.append(sorted(soln))

            elif soln_sum > target:
                return -1

            else:
                # dfs potential solution
                for i in range(len(candidates)):
                    new_soln = sorted(soln+[candidates[i]])
                    if str(new_soln) not in explored_dict:
                        feedback = dfs(new_soln, candidates[i:])
                        if feedback == -1:
                            break



        dfs([], candidates)

        return output

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        solve using backtracking

        start with set of candidates, dfs with new solution and remaining candidate set

        time complexity: O(N!/(N-k)!)
        space complexity: would be do to recursive calls, how many recursive calls? is it also O(N!)? that feels wrong

        """
        output = []
        
        def dfs(soln,candidates):
            if len(candidates) == 0:
                # add to solution
                output.append(soln)
            else:
                for i in range(len(candidates)):
                    remaining_candidates = candidates[0:i]+candidates[i+1:]
                    new_solution = soln+[candidates[i]]
                    dfs(new_solution,remaining_candidates)
                    
                    
        dfs([],nums)
        print(output)

        return output

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        """
        time complexity: O(2**N) as for each num in candidate we can either include or not
        space complexity: O(N) though less tidy on this
        """

        # params
        soln_dict = {}
        explored_dict = {}
        output = []
        candidates = sorted(candidates)
        new_candidates = []

        # if total candidates don't add to target return empty set
        if sum(candidates) < target:
            return []

        # remove candidates > target
        for i in candidates:
            if i <= target:
                new_candidates.append(i)

        def dfs(current_soln,remain_cand):
            sum_soln = sum(current_soln)
            current_soln = sorted(current_soln)
            str_current_soln = str(current_soln)

            # keep track of what has been explored
            explored_dict[str_current_soln] = 1


            # what to do next?
            if sum_soln == target and str_current_soln not in soln_dict:
                # add solution
                output.append(current_soln)
                soln_dict[str_current_soln] = 1
                print(output)
                return

            elif len(remain_cand) == 0:
                # stop explore this path
                return

            elif sum_soln > target:
                # stop exploring this path
                return

            else:
                # explore with remaining candidates
                for i in range(len(remain_cand)):
                    new_soln = sorted(current_soln + [remain_cand[i]])
                    new_cand = sorted(remain_cand[0:i] + remain_cand[i+1:])
                    if str(new_soln) not in explored_dict:
                        dfs(new_soln, new_cand)


        dfs([],new_candidates)
        return output