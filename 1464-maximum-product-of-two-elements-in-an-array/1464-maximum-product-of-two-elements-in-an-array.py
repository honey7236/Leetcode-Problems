class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_p = 0
        if n == 2:
            return (nums[0] - 1) * (nums[1] - 1)
        
        for i in range(n):
            for j in range(i+1,n): 
                product = (nums[i] - 1) * (nums[j] - 1)                
                if product > max_p:
                    max_p = product
        
        return max_p