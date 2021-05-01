class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
# 從兩邊開始算面積，接著選較小的那邊往中間一位，如此反覆
        start, end = 0, len(height)-1
        max_area = 0
        while(start != end):
            area = (end - start) * min(height[start], height[end])
            if area > max_area:
                max_area = area
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        
        return max_area

# s = Solution()
# s.maxArea([1,8,6,2,5,4,8,3,7])
# s.maxArea([1,1])
# s.maxArea([4,3,2,1,4])
# s.maxArea([1,2,1])
