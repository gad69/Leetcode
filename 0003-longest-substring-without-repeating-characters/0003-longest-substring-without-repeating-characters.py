class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset = set()
        l = 0
        r = 0
        size = 0  
        while r<len(s):
            
            while s[r] in charset:
                
                charset.remove(s[l])
                l = l+1
            charset.add(s[r])
            
            size = max(size,r-l+1)
            
            r = r+1
            
        return size
                
            
        

        