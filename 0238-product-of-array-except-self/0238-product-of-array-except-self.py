class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        arr = [1]*n
        for i in range(n):
            arr[i] = prefix_product
            prefix_product = nums[i]*prefix_product
            
        suffix_product = 1
        for j in range(n-1,-1,-1):
            arr[j] = arr[j]*suffix_product
            suffix_product = suffix_product*nums[j]
            
            
        return arr
            
            
            
        