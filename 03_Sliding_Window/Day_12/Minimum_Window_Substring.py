#https://leetcode.com/problems/minimum-window-substring/description/
"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

def fun(have, need):
    for i in range(256):
        if have[i] < need[i]:
            return False
    return True


def minWindow(s, t):
    n = len(s)
    m = len(t)
    have = [0] * 256
    need = [0] * 256

    if n < m:
        return ""

    if not t:
        return ""

    for i in range(m):
        need[ord(t[i])] += 1  #ord is to convert string into numeric character codes

    low, high = 0, 0
    res = float('inf')
    start = -1

    for high in range(n):
        have[ord(s[high])] += 1

        while fun(have, need):
            length = high - low + 1

            if res > length:
                res = length
                start = low

            have[ord(s[low])] -= 1
            low += 1

    if res == float('inf'):
        return ""

    return s[start:start + res]

s1 = "ADOBECODEBANC"
t1 = "ABC"

s2 = "a"
t2 = "a"

s3 = "a"
t3 = "aa"

print(minWindow(s1, t1))
print(minWindow(s2, t2))
print(minWindow(s3, t3))

#Time Complexity = O(n+m)
#Space Complexity = O(1)