class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if the number is negative, or a multiple of 10 but not 0
        if x < 0 or x % 10 == 0 and x !=0:
            return False
        
        revHalf = 0
        while x > revHalf:
            

            return True
        return True
#input
num = input("Enter number:")
x = int(num)
sol = Solution()
result = sol.isPalindrome(x)
print(result)