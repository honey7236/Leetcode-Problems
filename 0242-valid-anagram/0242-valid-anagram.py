class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        l2 = list(t)
        l.sort(), l2.sort()
        return l == l2

        