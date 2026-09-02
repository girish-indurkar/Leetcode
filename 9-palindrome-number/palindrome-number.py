class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        result = 0
        while num > 0:
            y = num%10
            result = result *10 + y
            num = num//10

        if result == x:
            return True
        else: 
            return False
            