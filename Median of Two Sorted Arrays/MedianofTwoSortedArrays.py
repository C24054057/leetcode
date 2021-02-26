class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s = nums1 + nums2
        s.sort()
        
        n = len(s)
        index = (n - 1) // 2

        if not n % 2:
            return (s[index] + s[index + 1]) / 2.0 # 要除2.0，leetcode才會正確
        else:
            return s[index]

# nums1 = [1, 3]
# nums2 = [2]
# nums1 = [1, 2]
# nums2 = [3, 4]
# nums1 = [0, 0]
# nums2 = [0, 0]
# nums1 = []
# nums2 = [1]
# nums1 = [2]
# nums2 = []

# s = Solution()
# print(s.findMedianSortedArrays(nums1, nums2))