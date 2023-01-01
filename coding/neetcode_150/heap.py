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

    def findKthLargest(self, nums: List[int], k: int) -> int:
    """
    time compelxity: N*log(k)
    space: O(k)
    """

        foo = []
        heapq.heapify(foo)
        for i in range(len(nums)):
            heapq.heappush(foo,nums[i])

            if len(foo) > k:
                heapq.heappop(foo)

        return heapq.heappop(foo)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        https://leetcode.com/problems/task-scheduler
        ### Examples
        * tasks = ["A","A","A","B","B","B"], n = 2
        [A,B] [1, 2]

        A -> B -> idle -> A -> B -> idle -> A -> B
        A, lookback n tasks and see if A is in there, if so wait until A is no longer there

        * tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
        * n = 2 so keep a queue of size 2
        * do one scan through the list and see that we have: 6 A's, 1 B, 1 C, 1 D, 1 E, 1 F, 1 G
        * keep a max heap that hold these in a priority queue

        queue = []
        max heap with A at root and, say B, C connected on either sides

        see what root node is --> check queue if that task is in the queue
            --> if no, do task
            --> if yes, see if there is another task that can be done and if so do that
            --> if yes and no other task available, wait cooldown period and continue

        ### Approach
        * create queue of size n
        * create heap that sorts based on count
            * req: create data structure with nested task and count --> [(6, A), (1, B), etc.]
        """
        # init vars
        q = deque([]) # use explicit deque otherise popleft is O(n)
        priority_queue = []
        count_dict = {}
        time = 0

        # update and use count_dict
        for i in tasks:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1

        # form priority_queue
        # [3,2,3,4,1]
        for key in count_dict:
            priority_queue.append(count_dict[key])

        # heapify
        heapq._heapify_max(priority_queue) # O(nlogn) but here it won't be greater than 26

        while priority_queue or q:
            # increase time counter
            time += 1

            # get root of max heap
            if priority_queue:
                val = heapq.heappop(priority_queue)
                new_val = val - 1
                heapq._heapify_max(priority_queue)

                if new_val:
                    # add back to queue
                    q.append([new_val, time + n])

            # pop from queue if condition met
            if q and q[0][1] == time:
                # add back to priority queue
                heapq.heappush(priority_queue, q.popleft()[0])
                heapq._heapify_max(priority_queue)
            
        return time
