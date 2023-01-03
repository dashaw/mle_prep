class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        [[0,30],[5,10],[15,20]]
        start = 0
        end = 30

        start = 5
        end = 10

        violation #1: there is another end > start, so cannot attend

        are there others?
        """

        if len(intervals) == 1:
            return True

        # sort
        intervals = sorted(intervals)

        for i in range(len(intervals)-1):
            start = intervals[i][0]
            end = intervals[i][1]

            next_start = intervals[i+1][0]
            next_end = intervals[i+1][1]

            if end > next_start:
                return False
            # check = [end > intervals[ind][0] and start <= intervals[ind][0] for ind in range(len(intervals)) if ind != i]

        return True

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        approach: we really only care about the max number of concurrent meetings at any one time

        1. sort by start time
        2. check if end of current > start time of next, if so there is overlap
        3. see how often this happens while pointed at current end time
        4. output max

        time complexicty = O(NlogN + N) --> O(NlogN)
        space complexity = O(N) --> 
        """

        # sorted
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        print('hey')
        cnt = 0
        s, e = 0, 0
        max_rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                cnt += 1
                s += 1
            else:
                cnt -= 1
                e += 1
            max_rooms = max(max_rooms, cnt)

        return max_rooms

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/insert-interval
        ### Examples
        * sorted by start
        * need to merge overlapping

        #### 1
        * intervals = [[1,3],[6,9]], newInterval = [2,5]
        * see that [2,5] -> start = 2
        * see that ordered array is [1,6]
        * insert new interval one place to right of first index it is greater than
        * [[1,3], [2,5], [6,9]]
        * observe the end time of one element to left = 3 and see if 2 < 3 -> it is so we need to merge
        * [[1,5]]
        * observe the start time of one element to the right of insert and see it is 6, 6 > 5 so do not need to merge
        * res = [[1,5], [6,9]]

        #### 2
        * intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        * start_new = 4
        * start_intervals = [1,3,6,8,12]
        * see that start_new should be placed at ind = 2 -> [1,3,4,6,8,12]
        * now check for merges, given no merges originally existed
        * for [4,8] we see start_new = 4, end_new = 8
        * check left for merges: 4 < 5 ? -> yes -> merge [[1,2],[3,8],[6,7]...], start_new = 3, end_new = 8
            * continue checking left: 3 < 2 -> no stop
        * check right for merges: 8 > 6 -> yes -> end_new = max(end_new, last element of this check) = 8
            * [[1,2],[3,8],[8,10],[12,16]]
            * check if end_new >= next start -> yes -> merge
                * end_new = 10

        * res = [[1,2],[3,10],[12,16]]

        ### Approach
        1. figure out where to place newInterval in terms of index (binary search = O(logn))
        2. merge left and update variables/intervals O(n/2?)
        3. merge right and update variables/intervals O(n)
        4. return result

        WRONG APPROACH(!)
        * notice that above we say we can use binary search = O(logn) to find insert position, so let's do that
        * but then we still need to merge left and right an unknown amount of times
        * in worst case these can be O(n)!
        * so why not just keep it simple and iterate through original array and compare conditions as is?
        """

        # init vars
        len_intervals = len(intervals)
        start_new = newInterval[0]
        end_new = newInterval[1]
        res = []

        # iterate through
        for i in range(len_intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > end:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
            
        res.append(newInterval)

        return res
