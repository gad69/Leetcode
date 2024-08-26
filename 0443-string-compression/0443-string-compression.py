class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 1
        count = 1

        while j<len(chars):
            if chars[j]==chars[j-1]:
                count = count+1


            elif chars[j]!=chars[j-1]:
                chars[i] = chars[j-1]
                i = i+1
                if count>1:
                    for s in str(count):
                        chars[i] = s
                        i = i+1
                count = 1

            j = j+1


        chars[i] = chars[j-1]
        i = i+1
        if count>1:
            for s in str(count):
                chars[i] = s
                i = i+1

        return i






        
        