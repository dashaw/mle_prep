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
