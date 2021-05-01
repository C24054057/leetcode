class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ''
        idx = 0
        if not strs: # list裡沒有單字
            return output
        while(True):
            flag = True
            check_letter = strs[0][idx:idx+1]
            for word in strs:
                # word的長度比idx短也算沒找到符合的prefix
                if idx >= len(word) or check_letter != word[idx:idx+1]:
                    flag = False
                    break
            if not flag:
                break
            output += check_letter
            idx += 1

        return output




# s = Solution()
# s.longestCommonPrefix(["flower","flow","flight"])
# s.longestCommonPrefix(["dog","racecar","car"])
# s.longestCommonPrefix([""])