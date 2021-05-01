class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        hash_table = dict()
        for i in range(numRows):
            hash_table[str(i)] = ''
        flag = 0
        amount = 1 # 決定+或-
        for letter in s:
            hash_table[str(flag)] += letter
            if flag == 0:
                amount = 1
            if flag == numRows - 1:
                amount = numRows - 1 # 等於-1
            flag = (flag + amount) % numRows

        output = ''
        for i in range(numRows):
            output += hash_table[str(i)]
        
        return output
        
            
        

# s = Solution()
# s.convert('PAYPALISHIRING', 4)
# s.convert('PAYPALISHIRING', 3)
# s.convert('A', 1)
