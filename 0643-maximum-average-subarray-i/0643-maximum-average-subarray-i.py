class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_sum = float('-inf')
        
        summ  =0
        left = 0
        right = 0
        
        while right<len(nums):
            summ = summ+nums[right]
            
            if right-left+1==k:
                max_sum = max(summ,max_sum)
                summ = summ - nums[left]
                left = left+1
                
            right+=1
            
        return max_sum/k
        
        
        