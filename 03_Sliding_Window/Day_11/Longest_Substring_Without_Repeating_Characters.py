#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from collections import defaultdict

def lengthOfLongestSubstring(s):
    f = defaultdict(int)
    low,high = 0, 0
    res = 0
    while(high<len(s)):
        f[s[high]] += 1 #HashMap
        k = high - low + 1
        while(len(f)<k):
            f[s[low]] -= 1
            if f[s[low]] < 1: #del char from HP which has 0 count
                del f[s[low]]
            low += 1
            k = high - low + 1
        if len(f) == k:
            length = high - low + 1
            res = max(res, length)
        high += 1

    return res if res != 0 else -1

s1 = "abcabcbb"

s2 = "bbbbb"

s3 = "pwwkew"

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))