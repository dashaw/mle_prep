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

    def rotate(self, nums: List[int], k: int) -> None:
        """
        https://leetcode.com/problems/rotate-array
        Do not return anything, modify nums in-place instead.
        Examples
        1. nums = [-1,-100,3,99], k = 2
        k = 1 --> [99,-1,-100,3]
        k = 2 --> [3,99,-1,-100]
        time = O(n)
        space = O(n)
        """

        # initial vars
        len_nums = len(nums)
        helper_nums = [0]*len_nums

        if k > len_nums:
            k = k % len_nums

        # perform rotations
        for i in range(len_nums):
            new_ind = i + k
            if new_ind > len_nums - 1:
                new_ind = new_ind % len_nums

            # update helper
            helper_nums[new_ind] = nums[i]

        # copy back
        for i in range(len_nums):
            nums[i] = helper_nums[i]

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
	https://leetcode.com/problems/boats-to-save-people
        Examples:
        people = [3,5,3,4], limit = 5
        -> [3], [3], [4], [5]

        people = [3,2,2,1], limit = 3
        [1,2,2,3,4,6] limit = 5
        [4,1]
        [2,2]
        [3]
        [6]
        -> find if there are two pairs that can fit under limit = [1,2]
        -> remaining = [2,3] --> find if there are two pairs taht can fit under limit --> no
        [[1,2],[2],[3]]
        
        Approach:
        1. sort list of people
        2. left_pointer = start, right_pointer = end
        3. see if sum <= limit --> yes then put those in a boat
        4. else move right_pointer to left, check again, etc.
        5. if left_pointer >= right_pointer there are no combinations so output individually
        time ~ O(n) + O(nlogn) for sort = O(nlogn)
        space ~ O(1)
        """

        # initial vars
        boat_cnt = 0
        people.sort()
        num_people = len(people)
        left_pointer = 0
        right_pointer = num_people - 1

        while left_pointer <= right_pointer:
            # potential value
            val = people[left_pointer] + people[right_pointer]

            # increment boat count
            boat_cnt += 1

            if val <= limit:
                # this is a combination that works, so also update left pointer to represent this
                left_pointer += 1

            # continue iterating backward
            right_pointer -=1

        # return
        return boat_cnt

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/4sum
        ### Example
        #### 1
        * nums = [1,0,-1,0,-2,2], target = 0
        [1,0,-1,0]
        [-2,2,0,0]
        [1,-1,-2,2]
        * what if this was sorted?
        * [-2,-1,0,0,1,2]
        * [-2], [-1,0,0,1,2]
        * [-2,-1], [0,0,1,2] -> [-2,-1,1,2]
        * [-2,0], [0,1,2] -> [-2,0,0,2]
        * [-2,0], [1,2] -> none
        * [-1], [0,0,1,2]
        * [-1,0], [0,1,2] - > [-1,0,0,1]
        time = O(n^3)
        space = O(n)?
        """
        # init vars
        len_nums = len(nums)
        nums.sort()
        res = []
        quad = []

        def _helper(k, start, target):
            if k != 2:
                for i in range(start, len_nums - k + 1):
                    quad.append(nums[i])
                    _helper(k-1, i+1, target - nums[i])
                    quad.pop()
                return
            l, r = start, len(nums)-1
            while l < r:
                l_val = nums[l]
                r_val = nums[r]
                if l_val + r_val > target:
                    r -= 1
                elif l_val + r_val < target:
                    l += 1  
                else:
                    cand = quad+ [l_val, r_val]
                    if cand not in res: res.append(quad+ [l_val, r_val])
                    l += 1

        # call search
        _helper(4, 0, target)

        return res
