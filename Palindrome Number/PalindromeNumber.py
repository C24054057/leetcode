class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x_rev = x[-1::-1]
        if x == x_rev:
            return True
        else:
            return False


# s = Solution()
# s.isPalindrome(121)
# s.isPalindrome(-121)
# s.isPalindrome(10)
# s.isPalindrome(-101)