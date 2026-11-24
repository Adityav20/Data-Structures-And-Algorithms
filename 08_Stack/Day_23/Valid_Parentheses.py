#https://leetcode.com/problems/valid-parentheses/description/
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""
def isValid(s):
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
            continue
        if not st:
            return False
        if s[i] == ')' and st[-1] == '(':
            st.pop()
        if s[i] == '}' and st[-1] == '{':
            st.pop()
        if s[i] == ']' and st[-1] == '[':
            st.pop()
    if st:
        return False
    return True

s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([])"
s5 = "([)]"
s6 = "[({})]"

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
print(isValid(s5))
print(isValid(s6))

#Time Complexity = O(n)
#Space Complexity = O(n)