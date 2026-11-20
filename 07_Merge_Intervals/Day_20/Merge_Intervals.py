#https://leetcode.com/problems/merge-intervals/description/
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""

def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort()  # Sort by start time
    start1 = intervals[0][0]
    end1 = intervals[0][1]
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




print(merge(intervals1))
print(merge(intervals2))
print(merge(intervals3))

#Time Complexity = O(nlogn)
#Space Complexity = O(n)