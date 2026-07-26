class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        ans2 = 0
        if n == 3:
            ans = nums[0] * nums[1] * nums[2]
            return ans
        
        ans = nums[n-1] * nums[n-2] * nums[n-3]
        ans2 = nums[0] * nums[1] * max(nums)

        if ans > ans2:
            return ans
        else:
            return ans2