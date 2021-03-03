class Solution:
    def romanToInt(self, s: str) -> int:
        rom_nm = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        int_nm = 0
        length = len(s)
        for i, letter in enumerate(s):
            if i < length-1 and rom_nm[letter] < rom_nm[s[i+1]]:
                int_nm -= rom_nm[letter]
            else:
                int_nm += rom_nm[letter]
        return int_nm
            

ob = Solution()
s = "IV"
print(ob.romanToInt(s))
