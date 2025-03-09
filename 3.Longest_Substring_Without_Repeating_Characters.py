class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 1
        length = 1
        left, right = 0, 1

        if len(s) == 0:
            return 0
        else:
            sub_s = s[left]

        while (right < len(s)):
            if s[right] in sub_s:
                left += 1
                right = left + 1
                sub_s = s[left]
                length = 1
            else:
                sub_s = sub_s + s[right]
                right += 1
                length += 1
                if length > maxLength:
                    maxLength = length
        return maxLength
