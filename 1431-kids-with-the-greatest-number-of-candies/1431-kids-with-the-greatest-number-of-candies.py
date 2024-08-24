class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        bol = []
        for i in candies:
            if i+extraCandies>=max_val:
                bol.append(True)
            else:
                bol.append(False)
                
        return bol