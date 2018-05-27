"""
===============================================================================================
Description
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

Have you met this question in a real interview?  
Example
Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].
Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].
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
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        
        if len(intervals) == 0 :
            return [ newInterval]
        
        answer = []
        appended = False
        intervals.sort(key=lambda tup: tup.start)
        for interval in intervals:
            if newInterval.start > interval.end:
                answer.append(interval)
                continue
            
            if newInterval.end < interval.start:
                answer.append(newInterval)
                startIndex = intervals.index(interval)
                answer.extend(intervals[startIndex:])
                appended = True
                break
            
            newInterval.start = min(newInterval.start, interval.start)
            newInterval.end = max(newInterval.end, interval.end)
            
        if not appended:
            answer.append(newInterval)
            
        return answer     
                