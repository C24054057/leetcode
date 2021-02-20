class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0: 
            negative = True
        x = abs(x)

        str_x = str(x)
        rev_x = int(str_x[::-1])

        if negative == True:
            rev_x = -rev_x

        if rev_x > 2 ** 31 - 1 or rev_x < - 2 ** 31:
            rev_x = 0

        

        print(rev_x)
        return rev_x






s = Solution()
s.reverse(-540000)