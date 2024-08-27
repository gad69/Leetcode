class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left = 0
        right = 0
        max_vowels = 0
        count = 0
        
        while right<len(s):
            if s[right] in {'a','e','i','o','u'}:
                count+=1
                
            if right-left+1==k:
                max_vowels =max(max_vowels,count)
                if s[left] in {'a','e','i','o','u'}:
                    count = count-1
                left = left+1
                           
            right = right+1
            
        return max_vowels
        
        
        