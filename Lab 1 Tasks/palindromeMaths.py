class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if the number is negative, or a multiple of 10 but not 0
        if x < 0 or (x % 10 == 0 and x !=0):
            return False
        
        revHalf = 0
        while x > revHalf:
            revHalf = revHalf * 10 + x % 10 
            x //= 10
        return x == revHalf or x == revHalf // 10



while True:
    #input
    num = input("Enter number or 'stop':")
    if num == "stop":
        break
    try:
        x = int(num)
        sol = Solution()
        result = sol.isPalindrome(x)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")