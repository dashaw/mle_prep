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
