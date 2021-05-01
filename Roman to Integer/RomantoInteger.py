class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        while(s):
            if s[0] == 'M':
                output += 1000
            # 百位數
            elif s[0:2] == 'CM':
                output += 900
                s = s[2:]
                continue
            elif s[0:2] == 'CD':
                output += 400
                s = s[2:]
                continue
            elif s[0] == 'D':
                output += 500
            elif s[0] == 'C':
                output += 100
            # 十位數
            elif s[0:2] == 'XC':
                output += 90
                s = s[2:]
                continue
            elif s[0:2] == 'XL':
                output += 40
                s = s[2:]
                continue
            elif s[0] == 'L':
                output += 50
            elif s[0] == 'X':
                output += 10
            # 個位數
            elif s[0:2] == 'IX':
                output += 9
                s = s[2:]
                continue
            elif s[0:2] == 'IV':
                output += 4
                s = s[2:]
                continue
            elif s[0] == 'V':
                output += 5
            elif s[0] == 'I':
                output += 1
            s = s[1:]
        
        return output

# s = Solution()
# s.romanToInt("III")
# s.romanToInt("IV")
# s.romanToInt("IX")
# s.romanToInt("LVIII")
# s.romanToInt("MCMXCIV")