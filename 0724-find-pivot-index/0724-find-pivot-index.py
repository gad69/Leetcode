class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0]*(len(nums))
        right_sum = [0]*(len(nums))
        
        left_sum[0]  = 0
        for i in range(1,len(nums)):
            left_sum[i] = nums[i-1]+left_sum[i-1]
            
        right_sum[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            right_sum[i] = right_sum[i+1]+nums[i+1]
            
            
        for i in range(len(nums)):
            if right_sum[i]==left_sum[i]:
                return i
            
        else:
            return -1
        
            
        
        
        