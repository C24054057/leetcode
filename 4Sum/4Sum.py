class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = list()
        nums.sort()

        used = set()
        for i in range(len(nums)):
            if nums[i] in used:
                continue
            used.add(nums[i])
            three_sum = target - nums[i]
            used_2 = set()
            for j in range(i+1, len(nums)):
                if nums[j] in used_2:
                    continue
                used_2.add(nums[j])
                hash_table, used_3 = dict(), set()
                for k in range(j+1, len(nums)):
                    if nums[k] in hash_table and nums[k] not in used_3:
                        output.append([nums[i], nums[j], nums[k], hash_table[nums[k]]])
                        used_3.add(nums[k])
                    else:
                        hash_table[three_sum - nums[j] - nums[k]] = nums[k]
        
        return output  




# s = Solution()
# s.fourSum(nums = [1,0,-1,0,-2,2], target = 0)
# s.fourSum(nums = [2,2,2,2,2], target = 8)
# s.fourSum(nums = [], target = 0)
# s.fourSum(nums = [-3,-2,-1,0,0,1,2,3], target = 0)
# s.fourSum(nums = [1, -1, -1, 1], target=0)