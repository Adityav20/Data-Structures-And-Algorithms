#https://leetcode.com/problems/insert-interval/description/
"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
def insert(intervals, newInterval):

    j = 0
    while j < len(intervals) and intervals[j][0] <= newInterval[0]:
        j += 1
    intervals.insert(j, newInterval)

    start1, end1 = intervals[0][0], intervals[0][1]
    merged = []
    
    for i in range(1, len(intervals)):
        start2, end2 = intervals[i][0], intervals[i][1]
        if end1 >= start2:  # Overlap
            end1 = max(end1, end2)

        else:
            merged.append([start1, end1])
            start1 = start2
            end1 = end2
    merged.append([start1, end1]) #To add last list 

    return merged

intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]

intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,8]

print(insert(intervals1, newInterval1))
print(insert(intervals2, newInterval2))