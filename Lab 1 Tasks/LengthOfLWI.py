class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lolw = 0
        i = len(s)-1
        while i >= 0 and s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            lolw += 1
            i -= 1
        return lolw


#input
s = input("Enter sentence:")
sol = Solution()
result = sol.lengthOfLastWord(s)
print(result)