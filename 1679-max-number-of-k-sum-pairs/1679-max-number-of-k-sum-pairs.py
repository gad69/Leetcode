class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        op = 0
        
        while left<right:
            summ = nums[left]+nums[right]
            if summ ==k:
                op+=1
                left+=1
                right-=1
                
            elif summ<k:
                left+=1
            else:
                right-=1
                
        return op
                
        