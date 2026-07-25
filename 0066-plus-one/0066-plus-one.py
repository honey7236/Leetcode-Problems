class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        num = 0
        for i in range(n):
            num = (num * 10) + digits[i]
        num += 1

        ans = [int(digit) for digit in str(num)]
        
        return ans