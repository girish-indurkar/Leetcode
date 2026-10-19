class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        i = 0
        while i < len(s):
            j = 0
            found = False

            while j < len(t):
                if s[i] == t[j]:
                    found = True
                    t = t[:j] + t[j+1:]
                    break
                j += 1

            if not found:
                return False

            i += 1

        return True