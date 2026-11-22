#https://leetcode.com/problems/interval-list-intersections/description/
"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""
def intervalIntersection(firstList, secondList):
    i, j = 0, 0
    result = []

    while i < len(firstList) and j < len(secondList):
        start_a, end_a = firstList[i]
        start_b, end_b = secondList[j]

        # overlap of two closed intervals
        lo, hi = max(start_a, start_b), min(end_a, end_b)
        if lo <= hi:
            result.append([lo, hi])

        # the interval that ends first can't overlap anything further
        if end_a < end_b:
            i += 1
        else:
            j += 1

    return result

firstList1 = [[0,2],[5,10],[13,23],[24,25]]
secondList1 = [[1,5],[8,12],[15,24],[25,26]]

firstList2 = [[1,3],[5,9]]
secondList2 = []

print(intervalIntersection(firstList1, secondList1))
print(intervalIntersection(firstList2, secondList2))

#Time Complexity = O(n)
#Space Complexity = O(1)