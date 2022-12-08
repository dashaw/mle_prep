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
