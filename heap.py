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

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        time complexity = n (build distance) + n*logn (build heap) + k*log(n) (extract and re-build)
        
        O(k*log(n))

        space = O(1)
        """
        dist = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist.append([((-x)**2 + (-y)**2)**(1/2),x,y])


        # heapify O(n*logn)
        heapq.heapify(dist)

        output = []
        for i in range(k):
            foo = heapq.heappop(dist)
            print(foo)
            output.append([foo[1],foo[2]])

        return output
