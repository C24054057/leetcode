import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip() # 去掉開頭的space
        sign = '+'
        # 判斷題目是否為空且題目有無正負號
        if s and (s[0] == '+' or s[0] == '-'):
            if '-' in s:
                sign = '-'
            s = s[1:]
        output = ''
        # 抽出數字，遇到第一個非數字則迴圈結束
        for ss in s:
            if not re.search(r'\d', ss):
                break
            output += ss
        # 沒抽到數字，返回0
        if not output:
            return 0
        # 回傳結果
        output = int(output)
        if sign == '-':
            output = -output
        if output > (2**31 - 1):
            return 2**31 - 1 
        elif output < -2**31:
            return -2**31
        else:
            return output



# s = Solution()
# print(s.myAtoi("   -42"))
# print(s.myAtoi("4193 with words"))
# print(s.myAtoi("words and 987"))
# print(s.myAtoi("-91283472332"))
# print(s.myAtoi(""))