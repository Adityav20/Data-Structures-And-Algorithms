#https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
"""
You are given a string s consisting only lowercase alphabets and an integer k. 
Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 

Example 1:
Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

Example 2:
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

Example 3:
Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
"""
from collections import defaultdict

def longestKSubstr(s, k):
    f = defaultdict(int)
    low,high = 0, 0
    res = 0
    while(high<len(s)):
        f[s[high]] += 1 #HashMap
        while(len(f)>k):
            f[s[low]] -= 1
            if f[s[low]] < 1: #del char from HP which has 0 count
                del f[s[low]]
            low += 1
        if len(f) == k:
            length = high - low + 1
            res = max(res, length)
        high += 1

    return res if res != 0 else -1

s1 = "aabacbebebe"
k1 = 3

s2 = "aaaa"
k2 = 2

s3 = "aabaaab"
k3 = 2

print(longestKSubstr(s1,k1))
print(longestKSubstr(s2,k2))
print(longestKSubstr(s3,k3))

#Time Complexity = O(n)
#Space Complexity = O(1)