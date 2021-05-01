class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        output = nums[-3] + nums[-2] + nums[-1] # 預設最大的三個數的和
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while(j<k):
                Sum = nums[i] + nums[j] + nums[k]
                if abs(Sum - target) < abs(output - target):
                    output = Sum
                if Sum == target:
                    return target
                elif Sum < target:
                    j += 1
                else:
                    k -= 1

        return output
            

# s = Solution()
# s.threeSumClosest([-1,2,1,-4], 1)
# s.threeSumClosest([1,-3,3,5,4,1], 1)
# s.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
# s.threeSumClosest([0,0,0], 1)