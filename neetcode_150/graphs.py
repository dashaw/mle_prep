class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        island = surrounded by water and formed by connecting adjacent lands horizontally or vertically
        approach:
        - figure out indexes of all 1's
        - do dfs or bfs and mark when able to get from 1 --> 1 another
        - when unable to get from to another, then add to num_islands and reset all need variables

        e.g., see there is 1 at [0,0]
        dfs until you can no more
        see which 1's weren't explored
        inc island count, start exploring them 

        time complexity = O(M*N)
        space complexity = O(M*N)
        """

        m = len(grid)
        n = len(grid[0])
        island_dict = {}
        ones_map = []
        explored_dict = {}
        num_ones = 0

        # create island dict
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ones_map.append([i,j])
                    num_ones += 1

        if num_ones == 0:
            return 0

        def dfs(r,c):
            # is this cell out of bounds?
            if r < 0 or c < 0 or r > m - 1 or c > n - 1:
                return
            elif grid[r][c] == "0":
                return
            elif grid[r][c] == "1":
                # found it, mark as part of given island cluster
                if str([r,c]) not in explored_dict.keys():
                    explored_dict[str([r,c])] = 1
                    dfs(r-1,c)
                    dfs(r+1,c)
                    dfs(r,c-1)
                    dfs(r,c+1)

        island_cnt = 0
        # search from a given starting spot
        while ones_map:
            foo = ones_map.pop(0)
            r = foo[0]
            c = foo[1]
            if str([r,c]) not in explored_dict.keys():
                island_cnt += 1
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
                print('here')

        return island_cnt


    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        approach
        - bfs graph, build new graph as we go

        time complexity = O(V+E)
        space complexity = O(V+E)
        """
        newToOld = {}

        def dfs(node):
            if node in newToOld:
                return newToOld[node]

            if node:
                copy = Node(node.val)
                newToOld[node] = copy

                for nei in node.neighbors:
                    copy.neighbors.append(dfs(nei))

                return copy

        return dfs(node)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        this is similar to the other island except in terms of num_islands we need to keep track of size
        
        approach
        1. loop through all grid locations once to find 1's positions
        2. dfs from 1's, keep track of vars
        
        time complexity = O(R*C) R rows, C columns
        space complexity = O(R*C)
        """

        m = len(grid)
        n = len(grid[0])
        num_ones = 0
        ones_dict = {}
        ones_queue = []

        if grid == [[1]]:
            return 1

        # initial scan of grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_ones += 1
                    ones_dict[str([i,j])] = 0
                    ones_queue.append([i,j]) 


        def dfs(r,c):
            nonlocal island_cnt, max_island

            str_pos = str([r,c])

            # check if out of bounds
            if r < 0 or c < 0 or r >= m or c >= n:
                return

            # check if we have already explored
            elif str_pos in explored_dict.keys():
                return 

            # check if cell == 1
            elif grid[r][c] == 1:
                island_cnt += 1
                explored_dict[str_pos] = 1
                ones_dict[str([r,c])] = island_cnt
                max_island = max(island_cnt, max_island)
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

                
        explored_dict = {}
        max_island = 0

        while ones_queue:
            foo = ones_queue.pop(0)
            island_cnt = 0
            foo_str = str(foo)

            if ones_dict[foo_str] == 0:
                # need to dfs
                r = foo[0]
                c = foo[1]
                island_cnt += 1
                max_island = max(max_island, island_cnt)
                explored_dict[foo_str] = 1
                ones_dict[str([r,c])] = island_cnt
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        return max_island

        """
        brute force
        go through each cell, loop through each other cell and see if it eventually leads to pacific and atlantic

        alt approach
        dfs from each cell, only continue dfs if height <= original dfs location
        so this would be m*n occurences of dfs
        also lots of duplication, could probably simplify

        time complexity = O(R*C)
        space complexity = O(R*C)
        """

        output_dict = {}
        explored_dict = {} # not sure exactly how this is used, but I imagine it will save some interim result + the max height encountered
        output = []
        m = len(heights)
        n = len(heights[0])

        def _early_stopping_dup(r,c):
            cell_str = str([r,c])

            if cell_str not in explored_dict:
                explored_dict[cell_str] = 1
                return False
            else:
                return True

        def _early_stopping_soln(r,c,original_r,original_c):
            new_cell_str = str([r,c])
            orig_cell_str = str([original_r,original_c])

            if new_cell_str in output_dict and 'atlantic' in output_dict[new_cell_str]['ocean'] and 'pacific' in output_dict[new_cell_str]['ocean']:
                output_dict[orig_cell_str] = {'r': original_r, 'c': original_c, 'ocean': ['atlantic','pacific']}
                return True

            else:
                return False

        def _add_solution(r,c,ocean):
            """
            for a solution we want to know
            1. starting cell
            2. max height encountered
            3. ocean if flowed into
            """
            cell_str = str([r,c])

            if cell_str not in output_dict:
                output_dict[cell_str] = {'r': r, 'c': c, 'ocean': [ocean]}
            else:
                output_dict[cell_str]['ocean'].append(ocean)


        def dfs(r,c,height,original_r,original_c):
            # pacific
            if r < 0 or c < 0:
                _add_solution(original_r,original_c,'pacific')
                return

            # atlantic
            elif r >= m or c >= n:
                _add_solution(original_r,original_c,'atlantic')
                return

            # not a valid explore
            elif heights[r][c] > height:
                return
            
            else:
                # explore or duplicate?
                early_stopping_flag = _early_stopping_dup(r,c)
                if early_stopping_flag: return

                # stop early because already successful path found
                early_stopping_flag = _early_stopping_soln(r,c,original_r,original_c)
                if early_stopping_flag: return

                # dfs
                dfs(r-1,c,heights[r][c],original_r,original_c)
                dfs(r+1,c,heights[r][c],original_r,original_c)
                dfs(r,c+1,heights[r][c],original_r,original_c)
                dfs(r,c-1,heights[r][c],original_r,original_c)

        for i in range(m):
            for j in range(n):
                explored_dict = {}
                dfs(i+1,j,heights[i][j],i,j)
                dfs(i-1,j,heights[i][j],i,j)
                dfs(i,j+1,heights[i][j],i,j)
                dfs(i,j-1,heights[i][j],i,j)
                
        # figure out which cells have both atlantic and pacific
        for k, v in output_dict.items():
            if 'pacific' in v['ocean'] and 'atlantic' in v['ocean']:
                output.append([v['r'], v['c']])

        return output
