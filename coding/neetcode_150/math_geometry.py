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
