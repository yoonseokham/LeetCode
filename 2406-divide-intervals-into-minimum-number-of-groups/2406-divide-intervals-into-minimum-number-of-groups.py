import collections
import heapq


class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        counter = collections.defaultdict(int)
        interval = collections.namedtuple('interval', 'start end')
        intervals = [interval(start, end) for start, end in sorted(intervals)]
        # end
        pq = []

        for interval in intervals:
            if pq and interval.start > pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval.end)
        return len(pq)