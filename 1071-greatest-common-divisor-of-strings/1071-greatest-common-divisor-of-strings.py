import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2:
            return str1


        elif len(str1)>len(str2):
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):],str2)
            else:
                return ""

        elif len(str2)> len(str1):
            if str2[:len(str1)] == str1:
                return self.gcdOfStrings(str1,str2[len(str1):])

            else:
                return ""

        else:
            return ""
                


















        