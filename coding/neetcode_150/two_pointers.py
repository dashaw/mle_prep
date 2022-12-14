class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        approach
        1. remove spaces, characters, lowercase
        2. reverse array in python using [::-1]
        3. see if reverse equals input

        time complexity = O(n)
        space complexity = O(n)
        """

        s = [c.lower() for c in s if c.isalnum()]
        s = ''.join(s)

        print(s)

        if s[::-1] == s:
            return True
        else:
            return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        index and value cannot be duplicate

        approach
        * convert to set?
        * brute force --> 

        [-1, 0, 1, 2, -1, 4]
        nested for loop
        look at ind, loop through rest of indices, then hash to see if there is a delta that works 

        time complexity: O(n+n^2) --> O(n^2)
        space complexity: O(n)
        """
        # vals
        len_nums = len(nums)
        sol_dict = {}
        sol = []

        # create hash table
        nums_dict = {}
        for i in range(len_nums):
            if nums[i] in nums_dict.keys():
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]] = [i]

        for i in range(len_nums):
            for j in (range(i+1,len_nums)):
                delta = -1*(nums[i] + nums[j])
                triplet = sorted([nums[i], nums[j], delta])
                if delta in nums_dict.keys() \
                and str(triplet) not in sol_dict:
                    delta_ind = set(nums_dict[delta]) - set([i,j])
                    if len(delta_ind) > 0:
                        sol_dict[str(triplet)] = 1
                        sol.append(triplet)

        return sol

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        [2,7,11,15]

        left_pointer = 0
        right_pointer 3

        val = 17

        left_pointer = 1

        time complexity = O(N?)
        space_complexity = O(1)

        """

        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            if left_pointer < 0 or right_pointer > len(numbers) - 1:
                return 'exit'

            val = numbers[left_pointer] + numbers[right_pointer]
            if val == target:
                return [left_pointer+1, right_pointer+1]

            elif val < target:
                left_pointer += 1

            elif val > target:
                right_pointer -= 1

        return -1

    def maxArea(self, height: List[int]) -> int:
        """
        approach
        - we want to find the max water that can be held for these combinations
        - the max water will be (window width)*(min(left window height, right window height))
        - we can take a sliding window approach to find the values

        brute force:
        for every element
          for every index 1:end

        this will probably be some O(N^2) approach
        what is a better way to find the combinations?

        left pointer = 0
        right pointer = end
        move inward accordingly
        water_held = get_water_held()

        time complexity = O(N) as we still are visiting elements only once
        space complexity = O(1)

        """
        def get_max_water(index_left,index_right):
            return min(height[index_left],height[index_right])*(index_right-index_left)

        left_pointer = 0
        len_height = len(height)
        right_pointer = len_height - 1
        max_water = 0

        while left_pointer < right_pointer:
            water_held = get_max_water(left_pointer,right_pointer)
            max_water = max(max_water, water_held)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water
