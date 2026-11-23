#https://www.geeksforgeeks.org/problems/attend-all-meetings-ii/1
"""
Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending time of ith meeting. Return the minimum number of rooms required to attend all meetings.

Note: A person can also attend a meeting if it's starting time is same as the previous meeting's ending time.

Example 1:
Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
Output: 1
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a single room.

Example 2:
Input: start[] = [2, 9, 6], end[] = [4, 12, 10]
Output: 2
Explanation: 1st and 2nd meetings at one room but for 3rd meeting one another room required.
"""
def minMeetingRooms(start, end):
    if len(start) < 1:
        return 0

    start.sort()
    end.sort()
    room = 0
    ans = 0
    i,j = 0,0
    while i < len(start) and j  < len(start):
        if start[i] < end[j]:
            room += 1
            ans = max(room, ans)
            i += 1
        else:
            room -= 1
            j += 1
    return ans

start1 = [1, 10, 7]
end1 = [4, 15, 10]

start2 = [2, 9, 6]
end2 = [4, 12, 10]

print(minMeetingRooms(start1,end1))
print(minMeetingRooms(start2,end2))