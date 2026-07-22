class Solution:
    def isalphanumeric(self, s):
        x = ord(s)
        if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
            return True

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p1 = 0
        p2 = len(s) - 1
        while p2>p1:
            if not self.isalphanumeric(s[p1]):
                p1 += 1

            elif not self.isalphanumeric(s[p2]):
                p2 -= 1

            elif s[p1] != s[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
