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

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        problems/surrounded-regions

        How do we know if a region is captured? It seems the only way it wouldn't be captured is
        if it is part of a region which has a border piece

        Approach
        - find the O's
        - find which O's are a part of the same "island" by graph traversal
        - find out if one of the O's is a border piece, if so --> not captured --> else, captured

        Time complexity: O(R*C)
        Space complexity: O(R*C) recursive stack calls
        """

        # set up vars
        oh_dict = {}
        cluster_dict = {} # let's use the idea of a cluster and label when a cluster has a border piece
        explored_dict = {} # keep track of cells we have searched
        num_ohs = 0
        cluster_cnt = 0 # label clusters of ohs
        m = len(board)
        n = len(board[0])
        target = "O"
        new_value = "X"

        # traverse board to find the ohs
        for i in range(m):
            for j in range(n):
                cell_str = str([i,j])
                if board[i][j] == target:
                    num_ohs += 1
                    oh_dict[cell_str] = {'r':i, 'c': j, 'cluster_assign': 0}

        # so now we know where the ohs are at, if they belong to a given cluster, and how many ohs there are
        def dfs(r,c):
            nonlocal cluster_cnt, cluster_dict, explored_dict

            # required vars
            cell_str = str([r,c])

            # have we explored this already?
            if cell_str in explored_dict:
                return

            # is this out of bounds?
            elif r < 0 or c < 0 or r > m - 1 or c > n - 1:
                cluster_dict[cluster_cnt]['border_piece'] = True

            # additional searching
            elif board[r][c] == target:
                explored_dict[cell_str] = 1 # update explore dict
                cluster_dict[cluster_cnt]['points'].append([r,c]) # update cluster assignment
                oh_dict[cell_str]['cluster_assign'] = cluster_cnt # update cluster assignment...again. 
                """
                todo: @darrens figure out if there is duplication in all this assignment
                """

                # keep exploring
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        # how do we want to search?
        for oh in oh_dict:
            r = oh_dict[oh]['r']
            c = oh_dict[oh]['c']
            cluster = oh_dict[oh]['cluster_assign']

            if cluster == 0:
                # then need to search as it hasn't been assigned yet
                cluster_cnt += 1
                cluster_dict[cluster_cnt] = {'points': [[r,c]], 'border_piece': False}
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)

        """
        questions:
        1. should we reset in data strucutres? example should we reset explored_dict after each outer-function call?

        answer: no, why: a cell is added to explored_dict only if it is already not in it and it equals target

        we do not want to re-explore ohs that have already been assigned to a cluster
        """

        # transform all ohs that do not belong to a cluster with a border piece to an ex
        for clust in cluster_dict:
            if cluster_dict[clust]['border_piece'] == False:
                # then need to update
                for p in cluster_dict[clust]['points']:
                    r = p[0]
                    c = p[1]
                    board[r][c] = new_value

        # return
        return board

    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        approach
        for every rotten cell
        perform 1 iteration of bfs, mark as rotten
        continue until all cells are bad
        time complexity = (On*m + n*m), space = O(n*m)
        """

        # initial vars
        good_cell_dict = {}
        rotten_cell_dict = {}
        m = len(grid)
        n = len(grid[0])

        def _check_status():
            good_dict = {}
            rotten_dict = {}

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        good_dict[str([i,j])] = [i,j]
                    
                    elif grid[i][j] == 2:
                        rotten_dict[str([i,j])] = [i,j]

            return good_dict, rotten_dict

        def _make_rotten(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                pass
            else:
                grid[i][j] = 2

        good_cell_dict, rotten_cell_dict = _check_status()
        num_good = len(good_cell_dict.keys()) 
        cnt = 0

        if num_good == 0:
            return 0

        while num_good > 0 and cnt < 10*10:
            for rotten in rotten_cell_dict:
                cell = rotten_cell_dict[rotten]
                row = cell[0]
                column = cell[1]

                _make_rotten(row+1, column)
                _make_rotten(row-1, column)
                _make_rotten(row, column+1)
                _make_rotten(row, column-1)
            
            cnt += 1

            # re-check rotten count
            good_cell_dict, rotten_cell_dict = _check_status()
            num_good = len(good_cell_dict.keys()) 

        return cnt if num_good == 0 else -1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Approach high-level:
        - feels like a straightforward BFS problem as we want the shortest distance
        - for each empty room, perform BFS until you reach a gate, keep track of how many iterations you've performed, once you reach a gate insert the iteration tracker # into the mxn grid
        - if there are no gates that can be reached then impute INF
          - how to tell if it is impossible to reach, check to see if there is any progress made for a given iteration and if nothing then stop BFS (or perhaps do check condition when coming back from BFS)
          BFS:
          create via queue O(1)

        Test cases
        assert wallsAndGates(rooms_mat) == expected_output
        """
        def _update_grid(row: int, col: int, bfs_cnt: int) -> None:
            curr_val = rooms[row][col]
            cand_val = bfs_cnt
            rooms[row][col] = min(curr_val, cand_val)

        def _add_rooms(row: int, col: int, bfs_cnt: int) -> None:
            if row < 0 or col < 0 or row >= m or col >= n or \
            rooms[row][col] == -1 or bfs_cnt > rooms[row][col]:
                return
            else:
                q.append([row,col,bfs_cnt])

        # initialize vars
        q = deque()
        visited = []
        m = len(rooms)
        n = len(rooms[0])

        # figure out where all the gates are
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append([i,j,0])
                    visited.append([i,j])

        # edge cases
        if len(q) == 0:
            return # come back to this
                     
        # for each gate, perform bfs and update grid cells as we go
        while q:
            # pop left
            foo = q.popleft()
            row, col, bfs_cnt = foo[0], foo[1], foo[2]
            pos_str = str([row,col])

            # update dist
            _update_grid(row, col, bfs_cnt)

            # continue bfs
            _add_rooms(row+1,col,bfs_cnt+1)
            _add_rooms(row-1,col,bfs_cnt+1)
            _add_rooms(row,col+1,bfs_cnt+1)
            _add_rooms(row,col-1,bfs_cnt+1)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Approach
        1. locate islands in grid2
          - iterate through all elements and keep track
          - perform DFS to find which 1's are part of which islands
        2. iterate through the islands in grid2
            - for each element, see if its value in grid1 is 1
            - if true for all cells in the island, then add to sub-count
        """
        # initial vars
        sub_island_cnt = 0
        island_marked = []
        m = len(grid2)
        n = len(grid2[0])

        # perform DFS to figure out which 1s map to which island
        def _dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or [row, col] in island_marked or grid2[row][col] == 0:
                return True

            # mark in list
            island_marked.append([row,col])

            # should we explore this later on to see if it is a valid sub-island?
            res = True
            if grid1[row][col] == 0:
                res = False

            # explore
            res = _dfs(row+1, col) and res
            res = _dfs(row-1, col) and res
            res = _dfs(row, col-1) and res
            res = _dfs(row, col+1) and res

            return res

        for i in range(m):
            for j in range(n):
                # see if we haven't mapped this to an island yet
                if grid2[i][j] == 1 and [i, j] not in island_marked and _dfs(i, j):
                    sub_island_cnt += 1

        # return result
        return sub_island_cnt

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        ### Examples
        https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
        n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]], happy_state_sum = 0 -> 1 -> 2
        {0: True, 1: True, 3: True, 2: True, 4: True, }
        * traverse from start -> 1, see that we encountered 0 and make note, update connection to go the other direction
        * traverse 1 to 3 see that it is leading away from 0 so update connection
        * see 3 doesn't go to any other node

        * see 4->5, need to switch

        n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
        start traversal:
        * 1 goes to 0, mark 1 as OK
        * 1 goes to 2, see that if we reverse we satisfy 2, so reverse
        * see 3 goes to 2 and is fine
        * see 3 goes to 4, reverse

        ### Approach
        1. iterate through connections and create hashmap of city-city connections
        2. begin by DFS from hashmap key = 0
        3. reverse connections as needed, keep a dictionary that maintains the status of each node 

        time O(n)
        space O(n)
        """
        # initialize vars
        connection_start = {}
        connection_end = {}
        num_happy_cities = 1
        num_changes = 0
        status_map = {}
        visited = set()
        edges = {(a,b) for a,b in connections}
        neighbors = {city:[] for city in range(n)}

        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # dfs
        def _dfs(city):
            nonlocal num_changes, edges, neighbors, visited

            # outgoing
            for neigh in neighbors[city]:
                if neigh in visited:
                    continue
                if (neigh, city) not in edges:
                    num_changes += 1

                visited.add(city)   
                _dfs(neigh)

        visited.add(0)
        _dfs(0)
        return num_changes

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/course-schedule-ii/
        ### Examples
        numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        [1: [0]
         2: [0]
         3: [1,2]
        ]
        [0,1,2,3]

        ### Approach
        1. create dictionary identifying all prereq for a given course
        2. dfs and once reaching a leaf, add to order array
        3. mark node as visited

        we need 3 core data strucute
        res = [] will be our output order
        cycle = set() will determine if we have encountered a cycle
        visit = [] if we have finished DFS on that nodes reqs and we know there are no dependencies
        time = O(V+E)
        space = O(V+E)
        """
        # init vars
        res = []
        course_dict = {}
        visit = set()
        cycle = set()
        cycle_flag = False
        total_courses = [i for i in range(numCourses)]

        # create initial mapping
        for val in prerequisites:
            course = val[0]
            prereq = val[1]
            if course in course_dict:
                course_dict[course].append(prereq)
            else:
                course_dict[course] = [prereq]

        # miss any?
        for i in range(numCourses):
            if i not in course_dict:
                course_dict[i] = []

        # edge case
        if prerequisites == []:
            return [i for i in range(numCourses)]

        # dfs
        def _dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for prereq in course_dict[course]:
                if _dfs(prereq) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        # iterate and call dfs
        for course in course_dict:
            if not _dfs(course):
                return []

        # miss anything?
        for i in range(numCourses):
            if i not in res:
                res.append(i)

        return res
