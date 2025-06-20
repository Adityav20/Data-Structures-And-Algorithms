class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_split = s.split()
        return len(word_split[-1])