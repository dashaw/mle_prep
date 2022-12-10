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
