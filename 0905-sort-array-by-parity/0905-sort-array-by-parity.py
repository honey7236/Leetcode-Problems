class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ponter = 0
        p_0 = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                nums[i], nums[ponter] = nums[ponter], nums[i]
                ponter += 1

        return nums