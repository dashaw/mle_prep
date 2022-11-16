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
