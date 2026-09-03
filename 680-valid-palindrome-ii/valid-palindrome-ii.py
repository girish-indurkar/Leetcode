class Solution:
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            left = s[i]
            right = s[j]

            if left != right:
                # deleting at most one character from it.
                  return (
                    self.isPalindrome(s,i + 1, j) or
                    self.isPalindrome(s, i, j - 1)
                )
            i += 1
            j -= 1   
        return True