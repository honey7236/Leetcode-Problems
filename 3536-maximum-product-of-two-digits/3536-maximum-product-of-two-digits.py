class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(digit) for digit in str(n)]
        max_p = 0

        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                p = l[i] * l[j]
                if max_p < p:
                    max_p = p
        return max_p