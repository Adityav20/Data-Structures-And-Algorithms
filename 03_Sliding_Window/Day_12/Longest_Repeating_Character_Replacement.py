#https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

from collections import defaultdict

def characterReplacement(s, k):
    f = defaultdict(int)
    low,high = 0, 0
    res = 0
    while(high<len(s)):
        f[s[high]] += 1 #HashMap
        length = high - low + 1
        max_freq = max(f.values())
        diff = length - max_freq
        while(diff>k):
            f[s[low]] -= 1
            if f[s[low]] < 1: #del char from HP which has 0 count
                del f[s[low]]
            low += 1
            length = high - low + 1
            max_freq = max(f.values())
            diff = length - max_freq
        res = max(res, length)
        high += 1

    return res if res != 0 else -1

s1 = "ABAB"
k1 = 2

s2 = "AABABBA"
k2 = 1

print(characterReplacement(s1, k1))
print(characterReplacement(s2, k2))

#Time Complexity = O(n)
#Space Complexity = O(1)