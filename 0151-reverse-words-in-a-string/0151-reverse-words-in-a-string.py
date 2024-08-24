class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse() # s = s[::-1] as reverse returns null

        return " ".join(s)