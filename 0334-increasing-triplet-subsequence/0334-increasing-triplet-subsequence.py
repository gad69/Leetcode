class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        max_val1 = float('inf')
        max_val2 = float('inf')
        
        for val in nums:
            if val<=max_val1:
                max_val1 = val
            elif val>max_val1 and val<=max_val2:
                max_val2 = val
            elif val>max_val2:
                return True
            else:
                return False
                
                
            
        
        
                
            
        
        
        
        
            
        