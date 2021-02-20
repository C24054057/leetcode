class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx_list = range(len(nums))
        for idx, num in enumerate(nums):
            residual = target - num
            for idx_a in idx_list[idx+1:]:
                if residual == nums[idx_a]:
                    return [idx, idx_a]


s = Solution()
print(s.twoSum([3,3], 6))