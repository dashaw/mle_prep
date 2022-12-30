class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time complexity = O

        """
        
        left = 0
        right = len(nums)-1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        if nums[0] > target or nums[-1] < target:
            return -1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        return - 1

    def searchMatrix(self, matrix, target):
        """
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ]

        target = 13

        """
        n = len(matrix)
        m = len(matrix[0])

        row_min = 0
        row_max = n - 1
        column_min = 0
        column_max = m - 1

        if matrix[0][0] > target or matrix[row_max][column_max] < target:
            return False

        if m == 1 and n == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False

        # find row
        while row_min < row_max:
            mid = (row_min + row_max)//2
            
            ref_value = matrix[mid][column_max]
            if ref_value == target:
                return True
            elif ref_value > target:
                row_max = mid
            elif ref_value < target:
                row_min = mid + 1
        
        # find column
        while column_min <= column_max:
            print(column_min)
            print(column_max)
            mid = (column_min + column_max)//2
            ref_value = matrix[row_min][mid]
            
            print(ref_value)
            
            if ref_value == target:
                return True

            elif ref_value > target:
                column_max = mid - 1

            elif ref_value < target:
                column_min = mid + 1
            
        return False

    def minEatingSpeed(self, piles, h):
        """
        piles = [3,6,7,11] h = 8
        
        [6,7,11] 1
        [2,7,11] 2
        [7,11] 3
        [3,11] 4
        [11] 5
        [7] 6
        [3] 7
        [] 8

        [11,7,6,3]
        [7,7,6,3] hour 1
        [3,7,6,3] 2
        [7,6,3] 3
        [3,6,3] 4
        [6,3] 5
        [2,3] 6
        [3] 7
        [8]

        lower_bound = 1
        upper_bound = max(piles)

        binary search --> check if valid --> based on result search upper or lower
        """

        num_piles = len(piles)
        max_banana = max(piles)
        lower = 1
        upper = max_banana
        min_k = int(10e9)

        def check_valid(k,bananas,h):
            hour_spent = 0
            
            if k == 0 :
                return False
                
            for pile in bananas:
                hour_spent += math.ceil(pile / k)
            
            if hour_spent <= h:
                return True
            else:
                return False

        """
        [30,11,23,4,20]
        [7,11,23,4,20] 1
        [11,23,4,20] 2
        [23,4,20] 3
        [4,20] 4
        [20] 5
        """

        solution_space = range(lower, upper+1) # [1,2,3,4,5,6]
        left = 0
        right = len(solution_space)

        while left <= right:
#             import pdb;pdb.set_trace()
            print(f'left: {left}')
            print(f'right: {right}')
            med = (left + right) // 2
            print(f'med: {med}')

            if check_valid(med,piles,h):
                print('valid solution')
                min_k = min(med, min_k)
                right = med - 1
            
            else:
                print('not valid')
                left = med + 1

        return min_k

    def search(self, nums: List[int], target: int) -> int:

        """
        approach: 4 pointers
        for given input list:
            - 1 equal far left
            - 1 equal middle left
            - 1 equal middle right
            - 1 equal far right

        time complexity = O(logn)
        space complexity = O(1)
        
        """

        def binary_search(left, right):
            print(left)
            print(right)

            # base case
            if left > right:
                return

            nonlocal target_ind
            # vars
            mid = ((right-left)//2) + left
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]

            # return case
            if mid_val == target:
                target_ind = mid
                return

            """
            [0,1,2,4,5,6,7,10,12]
            [7,10,12,1,4,5,6]

            target = 7

            mid_ind = 3 --> 1
            13 > target # so normally would search left, but here we should know that 
            but 13 > end value
            but also end of left value is greater than the target so still search left

            """

            if mid_val > target:
                if mid_val > right_val and left_val > target:
                    # search right
                    binary_search(mid+1, right)
                elif mid_val > right_val and left_val < target:
                    # search left
                    binary_search(left, mid-1)
                else:
                    # search left
                    binary_search(left, mid-1)

            elif mid_val < target:
                if mid_val < left_val and right_val < target:
                    # search left
                    binary_search(left, mid-1)
                elif mid_val > right_val and  right_val > target:
                    # search right
                    binary_search(mid+1, right)
                else:
                    # search right
                    binary_search(mid+1, right)
            
        left = 0
        right = len(nums) - 1
        target_ind = -1

        binary_search(left, right)

        return target_ind

    def findMin(self, nums: List[int]) -> int:
        """
	time complexity = O(logn)
        space complexity = O(logn)
        """
        min_val = math.inf

        # [4,5,6,7,0,1,2]

        def binary_search(left_ind: int, right_ind: int) -> None:
            nonlocal min_val

            # base cases
            if left_ind > right_ind:
                return
            
            mid_ind = (right_ind + left_ind)//2

            left_val = nums[left_ind]
            right_val = nums[right_ind]
            mid_val = nums[mid_ind]

            # new min?
            min_val = min(min_val, mid_val)

            # either our mid val is in the rotated side or not
            if mid_val >= left_val and right_val < left_val:
                # explore right
                binary_search(mid_ind + 1, right_ind)
            elif mid_val > left_val:
                # explore left
                binary_search(left_ind, mid_ind - 1)
            elif mid_val < left_val:
                # [6,0,1,2,3,4,5]
                # explore left
                binary_search(left_ind, mid_ind - 1)
        
        binary_search(0,len(nums)-1)
        return min_val

    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/single-element-in-a-sorted-array/description/
        [1,1,2,3,3,4,4,8,8]

        len = 9 [0, 8]
        mid = 9//2 --> 4

        - approach is to find mid point and look left and right by one index
        - mid_val = 3, left_val = 3, right_val = 4
        - mid_ind = 4, left_ind = 3, right_ind = 5
        - check if oddity is in upper
         - find which side has the agreement with mid val
         - in this case left
         - plus we see that len(left) = 5 --> odd --> keep exploring left

         [1,2,2,3,3]

         mid_ind = 5//2 = 2
         mid_val = 2
         left_val = 1
         right_val = 3
         no agreement --> output 2

         mid_ind = 5//2 = 2
         mid_val = 2
         left_val = 2
         right_val = 3
         look at left --> len([1,2,2]) --> odd --> keep exploring left



        nums = [1,1,2,3,3,4,4,8,8]
        len_nums = 9
        left = 0
        right = 8 --> 4
        mid = 4 --> 2
        mid_val = 3 --> 2
        left_val = 3 --> 1
        right_val = 4 --> 3
        (mid - left + 1) % 2 --> 1
        time complexity = O(logn)
        space complexity = O(1)

        """

        # initial vars
        len_nums = len(nums)
        left = 0
        right = len_nums - 1
        mid = ((right - left)//2) + left

        while mid < len_nums:
            mid = ((right - left)//2) + left

            if mid == 0 or mid == len_nums - 1:
                return nums[mid]

            mid_val = nums[mid]
            left_val = nums[mid-1]
            right_val = nums[mid+1]

            if mid_val == left_val:
                # something
                if (mid - left + 1) % 2 == 1:
                    # explore left
                    right = mid
                else:
                    # explore right
                    left = mid + 1
            elif mid_val == right_val:
                if (right - mid + 1) % 2 == 1:
                    # explore right
                    left = mid
                else:
                    # explore left
                    right = mid - 1
            else:
                return mid_val

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
        #### Examples
        * nums = [5,7,7,8,8,10], target = 8
        * find index of 8 = 3, find upper index = 4

        * nums = [5,7,7,7,7,8,8,10], target = 7
        * find index of a 7 = 4
        * look right to see if it continues that direction --> no, retain 4 as max
        * look to right to see if it continues in that direction --> yes, contain until reaching end

        #### Approach
        1. _binary_search(array, target)
        2. if not in index, output [-1, -1]
        3. else call _find_bounds(ind, target) to get lower and upper indices

	time complexity = O(logn) binary search + O(low n) for bounds
	space complexity ~ O(1) because in place
        """

        # initial vars
        res = [-1, -1]
        len_nums = len(nums)

        # check edge case
        # e.g., if target is below lower val or above upper val
        if len(nums) == 1 and nums[0] == target:
            return [0,0]

        def _find_bounds(ind: int, target: int) -> List[int]:
            left_ind = ind
            right_ind = ind

            # explore to left
            for i in range(ind)[::-1]:
                if nums[i] == target:
                    left_ind = min(left_ind, i)
                else:
                    break

            # explore to right
            for i in range(ind,len_nums):
                if nums[i] == target:
                    right_ind = max(right_ind, i)
                else:
                    break

            return [left_ind, right_ind]

        def _binary_search(arr, target):
            # initial vars
            len_arr = len(arr)
            left_pointer = 0
            right_pointer = len_arr - 1

            while left_pointer <= right_pointer:
                mid_pointer = left_pointer + ((right_pointer - left_pointer)//2)
                mid_val = arr[mid_pointer]

                if mid_val == target:
                    return mid_pointer
                elif mid_val < target:
                    left_pointer = mid_pointer + 1
                elif mid_val > target:
                    right_pointer = mid_pointer - 1

            return -1

        # get target index
        target_ind = _binary_search(nums, target)

        # bad case
        if target_ind == -1:
            return res
        else:
            return _find_bounds(target_ind, target)
