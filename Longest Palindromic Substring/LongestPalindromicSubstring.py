class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """      
        output = ''
        for i, start_letter in enumerate(s):
            j = len(s) - 1
            while(True):
                if i > j:
                    break
                if (start_letter == s[j] and # 判斷頭尾是否相同
                    s[i:j+1] == s[j-len(s):i-len(s)-1:-1] and # 判斷原句順著與倒著是否相同
                    len(s[i:j+1]) > len(output)): # 新的詞有沒有比output長
                    output = s[i:j+1]
                    break
                j -= 1
        return output             


# s = Solution()
# s.longestPalindrome("babad")
# s.longestPalindrome("cbbd")
# s.longestPalindrome("a")
# s.longestPalindrome("ac")
