class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        count_zeros = 0
        maxlen = 0
        
        while right<len(nums):
            
            if nums[right] ==0:
                count_zeros+=1
                
            while count_zeros>k:
                if nums[left] ==0:
                    count_zeros-=1
                left = left+1
                    
            maxlen = max(right-left+1,maxlen)
             
            right = right+1
            
            
        return maxlen
            
            
            
        
        
        
        
        
        
        
        