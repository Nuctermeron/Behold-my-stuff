class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31:
            return 0
        else:
            text_int = str(x)
            if x >= 0:
                reversed = text_int[::-1]
            else:
                temp = text_int[1:]
                temp2 = temp[::-1]
                reversed = "-" + temp2
            if int(reversed) >= 2**31-1 or  int(reversed) <= -2**31:
                return 0
            else:
                return(int(reversed))
            
sol = Solution()
a = sol.reverse(-251235)
print(a)