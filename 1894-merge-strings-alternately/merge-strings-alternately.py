class Solution:
    #Aditya
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        word1len = len(word1)
        word2len = len(word2)
        maxlen = max(word1len,word2len)
        count = 0

        while count <= maxlen:
            if count < word1len:
                merged += word1[count]
            if count < word2len:
                merged += word2[count]
            count += 1
        
        return merged    
        