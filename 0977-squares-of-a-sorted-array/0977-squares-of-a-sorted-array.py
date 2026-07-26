class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        square = []
        for i in nums:
            square.append(i*i)

        square.sort()
        return square