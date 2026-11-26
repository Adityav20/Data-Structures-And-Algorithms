#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""
def removeDuplicates(s, k):
    st = []

    for i in range(len(s)):
        c = s[i]
        if not st:
            st.append([c,1])
            continue
        if st[-1][0] != c:
            st.append([c, 1])
            continue
        if st[-1][1] < k-1:
            st[-1][1] += 1
            continue
        st.pop()

    return "".join(ch * count for ch, count in st)

s1 = "abcd"
k1 = 2

s2 = "deeedbbcccbdaa"
k2 = 3

s3 = "pbbcggttciiippooaais"
k3 = 2

print(removeDuplicates(s1, k1))
print(removeDuplicates(s2, k2))
print(removeDuplicates(s3, k3))

#Time Complexity = O(n)
#Space Complexity = O(n)