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


