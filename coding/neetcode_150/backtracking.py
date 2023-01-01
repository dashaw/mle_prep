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

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        approach:
        DFS for each cell as a starting point

        1. for every cell, initialize DFS
        2. explore in 4 directions for every cell (up, down, left right)
        3. if explored cell is out of bounds, return
        4. go at most N steps where N = length word
        5. there will be lots of duplication here
        6. 

	O(n*m + len(word) + n*m*4^len(word))

        """
        # initial vars
        len_word = len(word)
        m = len(board)
        n = len(board[0])
        found_word = False
        target_ind = 0
        board_counts = {}
        word_counts = {}

        # do we even have a chance? if it doesn't even make sense then return False
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                if c in board_counts:
                    board_counts[c] += 1
                else:
                    board_counts[c] = 1

        for c in word:
            if c in word_counts:
                word_counts[c] += 1
            else:
                word_counts[c] = 1

        
        for k in word_counts:
            if (k not in board_counts or
                board_counts[k] < word_counts[k]):
                return False
                

        # dfs
        def dfs(row: int, column: int, target_ind: int):
            nonlocal found_word

            # happy condition
            if target_ind == len(word):
                found_word = True
                return

            # combine stop conditions
            if (row < 0 or 
                column < 0 or 
                row >= m or 
                column >= n or
                board[row][column] != word[target_ind] or
                found_word):
                return

            # continue exploration
            temp = board[row][column] 
            board[row][column] = "#" # prior i was using a hash to determine if the new coordinate is already explored, but this is much quicker
            # explored_dict[str([row,column])] = 1

            """
            I've tried this with both hashmap and just setting the board char to "#",
            hash map still gets a timeout. I don't understand
            """

            dfs(row+1, column, target_ind+1)
            dfs(row-1, column, target_ind+1)
            dfs(row, column+1, target_ind+1)
            dfs(row, column-1, target_ind+1)
            
            board[row][column] = temp
            # del explored_dict[str([row,column])]


        for i in range(m):
            for j in range(n):
                dfs(i, j, target_ind)

        return found_word 

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
	https://leetcode.com/problems/combinations
        ### Examples
        1. n = 4, k = 2
            * range = [1,2,3,4]
            * combinations of 2 -> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        2. n = 4, k = 3
            * range = [1,2,3,4]
            * combinations of 3 -> [[1,2,3],[2,3,4],[1,3,4],[1,2,4]]

        ### Approach
        * backtracking
        * start at root = []
        * choose from remaining vals
        * once size of candidate solution = k -> add to solution set
        * stop dfs
        * time complexity = O(number of choices at each level ^ height)
        * = O(n^k)

        ### Test
        nums_range = [1,2,3,4]
        visited = [] -> [[], [1], [1,2], [1,2,3], [1,2,4], [1,3]]
        res = [[1,2,3], [1,2,4]]
        _dfs([], [1,2,3,4])
        _dfs([1], [2,3,4])
        _dfs([1,2], [3,4])
        _dfs([1,2,3], [4])
        _dfs([1,2,4], [3])
        _dfs([1,3], [2,4])
        _dfs([1,3,2]) -> don't go
        _
        """
        # init vars
        res = []
        visited = []

        # dfs helper function
        def _dfs(candidate: List[int], eligible_start_ind: int) -> None:
            nonlocal res, visited

            # see if length = k and if so add to candidate_soln
            if len(candidate) == k:
                res.append(candidate.copy())
                return

            # continue searching
            for i in range(eligible_start_ind, n + 1):
                candidate.append(i)
                _dfs(candidate, i+1)
                candidate.pop()

        # call dfs
        _dfs([], 1)

        # return
        return res
