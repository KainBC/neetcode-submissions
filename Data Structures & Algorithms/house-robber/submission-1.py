class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        maxProfit = [0] * len(nums)
        maxProfit[0] = nums[0]
        maxProfit[1] = nums[1]

        for i in range(2,len(nums)):
            maxVal = max(maxProfit[i-1],maxProfit[i-2]+ nums[i])
            if i >= 3:
                maxProfit[i] = max(maxVal,maxProfit[i-3]+ nums[i])
            else:
                maxProfit[i]= maxVal

        return max(maxProfit[-1], maxProfit[-2])