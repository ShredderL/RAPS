class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= 0:
            return False
        num = str(x)
        numRev = num[::-1]
        rev = int(numRev)

        if x == rev:
            return True
        else:
            return False

#input
num = input("Enter number:")
x = int(num)
sol = Solution()
result = sol.isPalindrome(x)
print(result)