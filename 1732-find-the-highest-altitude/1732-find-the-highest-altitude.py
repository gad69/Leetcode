class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = (len(gain)+1)*[0]
        
        altitudes[0] = 0
        for i in range(1,len(altitudes)):
            altitudes[i] = gain[i-1]+altitudes[i-1]

        return max(altitudes)
        