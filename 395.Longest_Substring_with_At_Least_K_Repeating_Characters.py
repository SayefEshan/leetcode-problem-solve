class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        countDict = {}
        charList = []
        tempString = ''
        longestSubString = ''
        for char in s:
            if char in countDict:
                countDict[char] += 1
            else:
                countDict[char] = 1

        for item in countDict.items():
            if item[1] >= k:
                charList.append(item[0])

        for i in range(len(s)):
            if s[i] in charList:
                tempString += s[i]
            else:
                if len(tempString) > len(longestSubString):
                    longestSubString = tempString
                tempString = ''

        if len(tempString) > len(longestSubString):
            longestSubString = tempString
        return len(longestSubString)
