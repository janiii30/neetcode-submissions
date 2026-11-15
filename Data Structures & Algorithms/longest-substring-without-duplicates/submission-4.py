class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ultimos_indices = {}
        izq = 0
        max_long = 0
        
        for der, char in enumerate(s):
            if char in ultimos_indices and ultimos_indices[char] >= izq:
                izq = ultimos_indices[char] + 1
            
            else:
                max_long = max(max_long, der-izq+1)
                
            ultimos_indices[char] = der
            
        return max_long
