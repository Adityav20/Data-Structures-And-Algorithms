#https://leetcode.com/problems/daily-temperatures/description/
"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""
def dailyTemperatures(temperatures):
    n = len(temperatures)
    st = []
    res = [0]*n
    st.append(n-1)
    for i in range(n-2, -1, -1):
        while st and temperatures[st[-1]] <= temperatures[i]:
            st.pop()
        if not st:
            res[i] = 0
        else:
            res[i] = st[-1] - i
        st.append(i)
    return res

temperatures1 = [73,74,75,71,69,72,76,73]
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]

print(dailyTemperatures(temperatures1))
print(dailyTemperatures(temperatures2))
print(dailyTemperatures(temperatures3))

#Time Complexity = O(n)
#Space Complexity = O(n)