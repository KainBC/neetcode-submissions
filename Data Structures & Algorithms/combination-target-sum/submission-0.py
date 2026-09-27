class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans= []
        def backtrack(idx, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            if idx >= len(nums) or total > target:
                return


            curr.append(nums[idx])
            backtrack(idx, curr, total + nums[idx])
            curr.pop()
            backtrack(idx+1, curr, total)

        backtrack(0, [], 0)

        return ans