"""
===============================================================================================
Given a collection of intervals, merge all overlapping intervals.

Have you met this question in a real interview?  
Example
Given intervals => merged intervals:

[                     [
  (1, 3),               (1, 6),
  (2, 6),      =>       (8, 10),
  (8, 10),              (15, 18)
  (15, 18)            ]
]
Challenge
O(n log n) time and O(1) extra space.
===============================================================================================
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if intervals is None or len(intervals) == 0:
            return []
        
        intervals.sort(key=lambda tup: tup.start)
        answer = []
        x = intervals[0]
        for i in range(1, len(intervals)):
            y = intervals[i]
            if x.end < y.start:
                answer.append(x)
                x = y
                continue
        
            x.start = min(x.start, y.start)
            x.end = max(x.end, y.end)
            
        answer.append(x)    
        return answer
        