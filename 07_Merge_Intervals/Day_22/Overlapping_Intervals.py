#https://www.geeksforgeeks.org/dsa/check-if-any-two-intervals-overlap-among-a-given-set-of-intervals/
"""
An interval is represented as a combination of start time and end time. Given a set of intervals, check if any two intervals intersect. 

Example 1: 
Input:  arr[] = [[1, 3], [5, 7], [2, 4], [6, 8]]
Output: true
Explanation: The intervals {1, 3} and {2, 4} overlap

Example 2: 
Input:  arr[] = [[1, 3], [7, 9], [4, 6], [10, 13]]
Output: false
Explanation: No pair of intervals overlap. 
"""
def isIntersect(intervals):
    if len(intervals) < 2:
        return False
    
    intervals.sort()
    start1, end1 = intervals[0]
    for i in range(1,len(intervals)):
        start2, end2 = intervals[i]
        if end1 >= start2:
            return True
        else:
            start1, end1 = intervals[i]

    return False

arr1 = [[1, 3], [5, 7], [2, 4], [6, 8]]
arr2 = [[1, 3], [7, 9], [4, 6], [10, 13]]

print(isIntersect(arr1))
print(isIntersect(arr2))

