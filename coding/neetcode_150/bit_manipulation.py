class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            print(f'a = {a}')
            print(f'i = {i}')
            a ^= i
            print(f'a = {a}')
            print('--------')
        return a

    def hammingWeight(self, n: int) -> int:
        """
        if num as binary ends in 0 then % 2 will result in 0, else it will end in 1 and % 2 will equal 1
        from there we can bit shift number by 1 position until it is empty
        """
        cnt = 0

        while n:
            print(n)
            if n % 2 != 0:
                cnt += 1
            n = n >> 1

        return cnt

    def countBits(self, n: int) -> List[int]:
        """
        time complexity = O(n)
        space complexity = O(1) output array does not count in space complexity
        """
        output = []
        for i in range(n+1):
            cnt = 0
            while i:
                cnt += i%2
                i = i >> 1
            output.append(cnt)

        return output

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        https://leetcode.com/problems/reverse-bits/
        reverse it -> so 1 -> 0
        0 -> 1

        so xor with a mask of FFFFF?
        """
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
