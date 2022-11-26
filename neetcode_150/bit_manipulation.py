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
