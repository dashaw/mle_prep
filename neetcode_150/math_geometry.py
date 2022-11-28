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
