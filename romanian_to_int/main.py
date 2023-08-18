class Solution(object):
    def romanToInt(self, s):
        r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        p = 0
        while p < len(s):
            if p < len(s) - 1 and r_dict[s[p]] < r_dict[s[p+1]]:
                result += r_dict[s[p+1]] - r_dict[s[p]]
                p += 2
            else:
                result += r_dict[s[p]]
                p += 1
        return result


r = Solution()
print(r.romanToInt("III"))
print(r.romanToInt("LVIII"))
print(r.romanToInt("MCMXCIV"))
