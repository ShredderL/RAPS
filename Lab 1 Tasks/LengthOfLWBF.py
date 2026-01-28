class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lolw = 0
        count = 0
        for i in s:
            if i == " ":
                count = 0
            else:
                count += 1
                lolw = count
        return lolw


#input
s = input("Enter sentence:")
sol = Solution()
result = sol.lengthOfLastWord(s)
print(result)