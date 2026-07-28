class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        ans = ""
        first = ""
        middle = ""
        if count == 1:
            return s

        for ch in sorted(count):
            first += ch * (count[ch] // 2)

            if count[ch] % 2:
                middle = ch

            ans = first + middle + first[::-1]
        return ans