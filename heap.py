class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        time complexity = O(NlogN)
        space complexity = O(N)
        """

        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)        
        return self.nums[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i]*-1

        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)*-1
            b = heapq.heappop(stones)*-1

            if a == b:
                pass
            else:
                res = (a - b)*-1
                heapq.heappush(stones, res)

        if len(stones) == 1:
            return stones[0]*-1
        else:
            return 0

