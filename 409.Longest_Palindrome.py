class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_s = {}
        center_found = False
        length = 0
        for i in s:
            if i in hash_s:
                hash_s[i] += 1
            else:
                hash_s[i] = 1
        for value in hash_s.values():
            if value == 1 and not center_found:
                length += 1
                center_found = True
            elif (value % 2 == 0):
                length += value
            else:
                if (center_found):
                    length += value - 1
                else:
                    length += value
                    center_found = True
        return length
