class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        time complexity = O(N)
        space complexity = O(1)
        """
        for i in range(len(digits))[::-1]:
            print(digits)
            print(i)
            val = digits[i]
            print(val)
            if val < 9:
                val += 1
                digits[i] = val
                break
            elif i == 0:
                # wait for next index
                digits[i] = 0
                digits = [1] + digits
            else:
                digits[i] =0

        return digits

    def isHappy(self, n: int) -> bool:


        """
        time: O(logn) consider n = 1e6 --> first round we go (worst case 1 million 9s) 81*1e6 = 81e6
        from 1 million digits to 8, so this has logn behavior
        space: O(logn)
        """

        cycle_dict = {}

        cnt = 0
        while n:
            if n == 1:
                return True

            new = 0
            for i in range(len(str(n))):
                foo = int(str(n)[i])
                new += foo**2
            n = new

            if n in cycle_dict:
                return False
            else:
                cycle_dict[n] = 1

    def sampleStats(self, count: List[int]) -> List[float]:
        """
        https://leetcode.com/problems/statistics-from-a-large-sample/description/

        approach:
        - iterate through the count List
        - for the first non-zero index we encounter --> store as index = min value
        - for each index --> add appropriate value to cumulative sum to calculate mean
        - for each index --> count number of results that are there and use this to calculate mode
        - for the last non-zero index we encounter --> store as index = max value

        - for the median, use this info after iterating all the way through the list of elements
        
        [0,1,3,4]
        1,2,2,2,3,3,3,3 --> length = 8
        even --> between index 8/2 and 8/2 + 1

        "need index 4" --> go to bucket 3
        [1,2,2,3,3] len = 5, 5//2 = 2 + 1 == 3 

        time complexity = O(n + n) = O(n)
        space complexity ~ O(n)
        """

        def _calculate_medium(pos1, pos2, index_tracker):
            for i in range(len(index_tracker)):
                lower = index_tracker[i][0]
                upper = index_tracker[i][1]
                ind = index_tracker[i][2]

                # figure out where pos1 occurs
                if pos1 > lower and pos1 <= upper:
                    pos1_ind = ind

                # figure out where pos2 occurs
                if pos2 > lower and pos2 <= upper:
                    pos2_ind = ind

            # take average of pos1, pos2
            return (pos1_ind + pos2_ind) / 2

        # vars
        cnt = 0
        cumulative_sum = 0
        cumulative_cnt = 0
        mode_cnt = 0
        index_tracker = []

        for i in range(len(count)):
            if count[i] > 0:
                if cnt == 0:
                    # save as min
                    minimum = i
                
                cnt += 1

                # cumulative tracker
                index_tracker.append([cumulative_cnt, cumulative_cnt+count[i], i])
                
                # running maximum
                maximum = i

                # cumulative_sum
                cumulative_sum += count[i]*i
                cumulative_cnt += count[i]

                # mode
                if count[i] > mode_cnt:
                    mode = i
                    mode_cnt = count[i]

        # calculate mean
        mean = cumulative_sum/cumulative_cnt
        median = 0

        # calculate median
        mod_len = cumulative_cnt % 2
        odd_flag = False if mod_len == 0 else True
        if odd_flag:
            # can extract median straightforward
            pos1 = (cumulative_cnt//2) + 1
            pos2 = pos1
        else:
            # need to isolate for middle two elements
            pos1 = cumulative_cnt/2
            pos2 = pos1 + 1

        median = _calculate_medium(pos1, pos2, index_tracker)

        return [minimum, maximum, mean, median, mode]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/spiral-matrix
        ### Examples
        * mxn matrix
        * return elements in spiral order

        matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
        * [1,2,3,6,9,8,7,4,5]

        matrix = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]
        ]
        * [1,2,3,4,8,12,11,10,9,5,6,7]
        * go across top row, go down last column, go across bottom row, go up to [0+1] row and go across, go down [3-1] column, repeat

        matrix = [
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16,17]
                ]        
        * row = 0, go from column 0:n
            * [1,2,3,4]
        * column = n -> go down column
            * [1,2,3,4,8,12,17]
        * column = n, row = m -> go right->across row = m ->
            * [1,2,3,4,8,12,17,16,15,14,13]
        * increase bottom_row += 1 --> 1 go across this to n-1 position
            * [1,2,3,4,8,12,17,16,15,14,13,]
        * column = 0 -> go up until lower_row marker 
            * [1,2,3,4,8,12,17,16,15,14,13,9,5]
        * continue

        seems we have at least 4 ints we need to maintain:
        row_lower = 0
        row_upper = m - 1
        column_lower = 0
        column_upper = n - 1
        * pattern:
            1. print(row_lower from column_lower:column_upper), row_lower += 1
            2. print(column_upper from row_lower:row_upper), column_upper -= 1
            3. print(row_upper, column_upper:column_lower), row_upper -= 1
            4. print(column_lower, row_upper:row_lower), column_lower += 1

        ### Approach
        fix row_lower: iterate across columns
        fix column_upper: iterate across rows
        fix row_upper: iterate across columns
        fix column_lower: iterate across columns

        while row_lower < row_upper and column_lower < column_upper:
            # do left_right traversal row
            # do top bottom traversal column
            # do right to left traversal row
            # do bottom to top traversal column

        ### Test
        matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
        m = 3
        n = 3
        row_lower = 0 -> 1 -> 2
        row_upper = 3 -> 2 -> 2
        column_lower = 0 -> 1
        column_upper = 3 -> 2 -> 1

        row_lower = 0, c:[0,1,2]
        [1,2,3]

        column_upper = 3-1 = 2, r:[1,2]
        [1,2,3,6,9]

        row_upper = 3-1=2, c:[0,1] -> [1,0]
        [1,2,3,6,9,8,7]

        column_lower = 0,: r:[1]
        [1,2,3,6,9,8,7,4]

        row_lower = 1, c:[1]
        [1,2,3,6,9,8,7,4]

        column_upper = 2, r:
        """
        # init vars
        m = len(matrix)
        n = len(matrix[0])
        row_lower = 0
        row_upper = m
        column_lower = 0
        column_upper = n
        res = []
        visited = {}

        while row_lower < row_upper and column_lower < column_upper: # and or or condition?
            # do left->right traversal row
            for c in range(column_lower,column_upper):
                res.append(matrix[row_lower][c])
            row_lower += 1

            if not (row_lower < row_upper and column_lower < column_upper):
                break

            # do top->bottom traversal column
            for r in range(row_lower,row_upper):
                res.append(matrix[r][column_upper-1])
            column_upper -= 1

            if not (row_lower < row_upper and column_lower < column_upper):
                break

            # do right->left traversal row
            for c in range(column_lower, column_upper)[::-1]:
                res.append(matrix[row_upper-1][c])
            row_upper -= 1

            if not (row_lower < row_upper and column_lower < column_upper):
                break

            # do bottom->top traversal column
            for r in range(row_lower, row_upper)[::-1]:
                res.append(matrix[r][column_lower])
            column_lower += 1

        # return
        return res

class Solution:
    # https://leetcode.com/problems/random-pick-with-weight
    # O(n)

    def __init__(self, w: List[int]):
        self.w = w
        self.len_w = len(w)
        self.cum_weights = []
        self.total = 0

        # [1,5,2]
        # [1, 6, 8]

        for i in range(self.len_w):
            self.cum_weights.append(w[i] + self.total)
            self.total += self.w[i]

    def pickIndex(self) -> int:
        target = self.total*random()
        res = 0
        for ind, val in enumerate(self.cum_weights):
            if target < val:
                return ind
