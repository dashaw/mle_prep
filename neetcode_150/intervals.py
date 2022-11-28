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
