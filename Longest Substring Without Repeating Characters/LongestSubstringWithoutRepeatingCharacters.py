class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_substring = ''
        cur_substring = ''
        for l in s:
            if l in cur_substring:
                if len(cur_substring) > len(max_substring):
                    max_substring = cur_substring
                cur_substring = cur_substring[cur_substring.index(l) + 1:] # 把前面的l去掉，留下後面的子字串
            cur_substring += l

# 更新最後一次max_substring
        if len(cur_substring) > len(max_substring):
            max_substring = cur_substring
        count = len(max_substring)
        # print(max_substring)
        # print(count)
        return count


# inp = 'abcabcbb'
# inp = 'bbbbb'
# inp = 'pwwkew'
# inp = ''
# inp = ' '
# inp = 'dvdf'
# s = Solution()
# s.lengthOfLongestSubstring(inp)