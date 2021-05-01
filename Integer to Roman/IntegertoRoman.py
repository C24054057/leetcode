class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ''
        # 轉換千位數
        thousand = int(num / 1000)
        for _ in range(thousand):
            output += 'M'
        # 轉換百位數
        hundred = int(num % 1000 / 100)
        if hundred == 9:
            output += 'CM'
        elif hundred == 4:
            output += 'CD'
        else:
            if hundred >= 5:
                output += 'D'
                hundred -= 5
            for _ in range(hundred):
                output += 'C'
        # 轉換十位數
        ten = int(num % 100 / 10)
        if ten == 9:
            output += 'XC'
        elif ten == 4:
            output += 'XL'
        else:
            if ten >= 5:
                output += 'L'
                ten -= 5
            for _ in range(ten):
                output += 'X'
        # 轉換個位數
        unit = int(num % 10)
        if unit == 9:
            output += 'IX'
        elif unit == 4:
            output += 'IV'
        else:
            if unit >= 5:
                output += 'V'
                unit -= 5
            for _ in range(unit):
                output += 'I'

        print(output)
        return(output)

# s = Solution()
# s.intToRoman(3)
# s.intToRoman(4)
# s.intToRoman(9)
# s.intToRoman(58)
# s.intToRoman(1994)