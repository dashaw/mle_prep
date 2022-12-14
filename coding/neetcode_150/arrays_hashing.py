"""
storing neetcode 150 solutions for Arrays & Hashing problems
"""

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/description/
        output k most requent elements

        Args:
          nums (List[int])
          k (int)

        Returns:
          List[int]

        Approach:
          1. pass through the array and build hash-table
          2. loop through hash table and keep/not based on value
        """

        element_dict = {}
        element_array = []
        for i in nums:
            if i not in element_dict.keys():
                element_dict[i] = 1
                element_array.append(i)
            else:
                element_dict[i] += 1

        # bubble sort
        swap_flag = True
        num_uniques = len(element_array)
        
        while swap_flag:
            swap_cnt = 0
            for i in range(num_uniques-1):
                crnt_ind = i
                nxt_ind = i+1
                crnt_num = element_array[crnt_ind]
                nxt_num = element_array[nxt_ind]
                crnt_val = element_dict[crnt_num]
                nxt_val = element_dict[nxt_num]

                if crnt_val < nxt_val:
                    print(f"{crnt_val}, {nxt_val}")
                    swap_cnt += 1
                    # then swap positions
                    element_array[crnt_ind] = nxt_num
                    element_array[nxt_ind] = crnt_num
                else:
                    # keep things how they are
                    pass

            if swap_cnt == 0:
                swap_flag = False
          
        return element_array[0:k]

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/

        Args:
          nums (List[int]): array of integers

        Returns:
           True if duplicates
        """
        num_dict = {}
        for i in nums:
            if i in num_dict.keys():
                return True
            else:
                num_dict[i] = 'found'

        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-consecutive-sequence/description/

        Args:
            nums (List[int])

        Returns:
            num_sequence

        Approach
            1. find unique elements
            2. sort
            3. go through array, check if consecutive, keep track output
        """
        # get unique
        nums_dict = {}
        for i in nums:
            if i not in nums_dict.keys():
                nums_dict[i] = 1
        
        nums_set = []
        for i in nums_dict.keys():
            nums_set.append(i)

        len_nums_set = len(nums_set)

        """
        go through set, see if it has a left neighbor
        if no left neighbor, it is start of consecutive, 
        loop through to see where it sends
        """
        max_consecutive = 0

        if len_nums_set == 0:
            return 0

        for i in nums_set:
            if nums_dict.get(i-1,0) == 0:
                # no left neighbor
                consecutive_flag = True
                num_consecutive = 1
                nxt_num = i + 1
                while consecutive_flag:
                    if nums_dict.get(nxt_num,0) == 1:
                        num_consecutive += 1
                        nxt_num += 1
                    else:
                        consecutive_flag = False
                
                if num_consecutive > max_consecutive:
                    max_consecutive = num_consecutive

        return max_consecutive

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/product-of-array-except-self/description/

        example [1,2,3,4]
        [2*3*4,1*3*4,1*2*4,1*2*3]

        prefix = [1,2,6,24]

        postfix = [1,24,12,4]

        brute force:
        for i -> 1:n
            for j -> 1:n
            perform multiplcation but skip ith element

        [[2,3,4],[1,3,4],[1,2,4],[1,2,3]]
        """
        # initialize
        len_nums = len(nums)
        pre_array = [0]*len_nums
        post_array = [0]*len_nums

        # seed
        pre_array[0] = nums[0]
        post_array[len_nums-1] = nums[len_nums-1]
   
        """
        nums = [1,2,3,4]
        post_array = [0,0,0,4]
        len_nums = 4
        i = 1

        pre_array = [1,2,6,24]

        post_array = [24,24,12,4]

        answer = [24,1*12,2*4]
        """

        # cumulative multiplication
        for i in range(1,len_nums):
            pre_array[i] = pre_array[i-1]*nums[i]
            post_array[len_nums-i-1] = post_array[len_nums-i]*nums[len_nums-i-1]
        print(pre_array)
        print(post_array)

        answer = []
        answer.append(post_array[1])
        for i in range(1,len_nums-1):
            answer.append(pre_array[i-1]*post_array[i+1])
        answer.append(pre_array[len_nums-2])

        return answer

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2,7,11,15,3] target = 10

        [1,4]

        brute force
        nested for loop

        time complexity = O(n**2)
        space complexity = O(1)
        """
        l_nums = len(nums)

        for i in range(l_nums):
            for j in range(i+1,l_nums):
                if nums[i] + nums[j] == target:
                    return [i,j]


class Codec:
    """
    https://leetcode.com/problems/encode-and-decode-strings
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode_str = ""
        for i in strs:
            encode_str += i
            encode_str += "<eos>"

        return encode_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decode_array = []
        ind_str = ""
        for i in s:
            ind_str+=i
            if len(ind_str)>= 5 and ind_str[-5:] == '<eos>':
                decode_array.append(ind_str[:-5])
                ind_str = ""
                
        return decode_array

    def isAnagram(self, s: str, t: str) -> bool:
        """
        1. all of chars of t in s
        2. all original letters in s used exactly once

        linear time and space complexity as we have to loop through and store dictionary --> O(n) for n = length of s, t
        """
        s_dict = {}
        for char in list(s):
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in list(t):
            if char in s_dict:
                if s_dict[char] == 1:
                    del s_dict[char]
                else:
                    s_dict[char] -= 1
            else:
                return False

        if len(s_dict.keys()) == 0:
            return True
        else:
            return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        approach
        1. sort
        2. hash
        3. group same hashes

        time complexity = O(N*log(N)) due to python sort
        space = O(N)
        """
        sorted_dict = {}

        for w in strs:
            w_sorted = sorted(w)
            w_key = str(w_sorted)
            if w_key in sorted_dict:
                sorted_dict[w_key].append(w)
            else:
                sorted_dict[w_key] = [w]

        
        # format result
        res = []
        for k,v in sorted_dict.items():
            res.append(v)

        return res

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fn_dict = {}
        for i in paths:
            foo = i.split(" ")
            root = foo[0]
            files = foo[1:]
            for f in files:
                fn_content = f.split("(")[1].split(")")[0]
                fn = f.split("(")[0]

                if fn_content in fn_dict:
                    fn_dict[fn_content].append(root+"/"+fn)
                else:
                    fn_dict[fn_content] = [root+"/"+fn]
        
        res = []
        for k,v in fn_dict.items():
            if len(v) > 1:
                res.append(v)
        
        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        https://leetcode.com/problems/valid-sudoku/
        constraints:
        1. each row much contain the digits 1-9 w/o repetition
        2. each column must contain the digits 1-9 w/o repetition
        3. each of the nine 3x3 sub-boxes must contian the digits 1-9 w/o repetition

        -can be partially filled (but still must meet constraints)
        -board is always 9x9

        brute force:
        go through each row and see if constaint 1 is met
        go through each column and see if constaint 2 is met
        go through each 3x3 box and see if constraint 3 is met

        time O(n*m)
        space O(n*m)
        """
        # initial vars
        valid_solution = True
        sub_box_constraint = {}
        row_constraint = {}
        column_constraint = {}
        sub_box_map = {}
        m = len(board)
        n = len(board[0])

        # initialize dicts
        for i in range(m):
            row_constraint[i] = []
            column_constraint[i] = []

        for i in range(9):
            sub_box_constraint[i] = []

        sub_box_cnt = 0
        for i in range(3):
            for j in range(3):
                sub_box_map[str([i,j])] = sub_box_cnt
                sub_box_cnt += 1

        for i in range(m):
            for j in range(n):
                val = board[i][j]

                if val != ".":
                    # check row
                    if val in row_constraint[i]:
                        valid_solution = False
                        break
                    else:
                        row_constraint[i].append(val)

                    # check column
                    if val in column_constraint[j]:
                        valid_solution = False
                        break
                    else:
                        column_constraint[j].append(val)

                    # check sub-grid
                    # get sub-grid number
                    sub_row = i//3
                    sub_column = j//3
                    box_str = str([sub_row,sub_column])
                    box_num = sub_box_map[box_str]
                    if val in sub_box_constraint[box_num]:
                        valid_solution = False
                        break
                    else:
                        sub_box_constraint[box_num].append(val)


        # return
        return valid_solution

    def sortColors(self, nums: List[int]) -> None:
        """
        https://leetcode.com/problems/sort-colors/
        Do not return anything, modify nums in-place instead.

        Approach
        * bubble sort O(n^2)

        [2, 0, 2, 1, 1, 0]
        [0, 2, 2, 1, 1, 0]
        [0, 2, 1, 2, 1, 0]
        [0, 2, 1, 1, 2, 0]
        [0, 2, 1, 1, 0, 2]
        time = O(N^2)
        space = O(1)
        """
        # initial vars
        sorted_flag = True
        len_nums = len(nums)

        while sorted_flag:
            sorted_flag = False

            for i in range(len_nums-1):
                if nums[i] > nums[i+1]:
                    # swap
                    temp = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = temp
                    sorted_flag = True

        return nums

    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/brick-wall/discussion/
        [
        [1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]
        ]

        [1,3,5,6],
        [3,4,6],
        [1,4,6],
        [2,6],
        [3,4,6],
        [1,4,5,6]

        ind = 1
        cnt = 3

        ind = 2
        cnt = 5

        ind = 3
        cnt = 3

        ind = 4
        cnt = 2

        O(n^2)

        is there a simpler approach?
        """

        # init vars
        cum_val = sum(wall[0])
        m = len(wall)
        n = len(wall[0])
        max_cells = 0
        res = 0
        width_dict = {}

        # form cumulative
        for i in range(m):
            width = 0
            max_cells = max(max_cells,len(wall[i]))
            for j in range(0,len(wall[i])):
                width += wall[i][j]
                width_dict.update({width: width_dict.get(width,0)+1})

        if max_cells == 1:
            return m

        # figure out lowest val
        for key in width_dict:
            if key != cum_val:
                res = max(res, width_dict[key])

        return m - res
