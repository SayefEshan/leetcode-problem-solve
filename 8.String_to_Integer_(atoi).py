class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''
        sign = 1
        leading_sign = False
        if len(s) == 0:
            return 0
        s = s.strip()
        print(s)
        for i in range(len(s)):
            if s[i] == '-' and result == '' and not leading_sign:
                sign = -1
                leading_sign = True
            elif s[i] == '+' and result == '' and not leading_sign:
                sign = 1
                leading_sign = True
            elif '0' <= s[i] <= '9':
                result += s[i]
            else:
                break

        result = 0 if result == '' else int(result) * sign
        if -2**31 > result:
            return -2**31
        elif 2**31 - 1 < result:
            return 2**31 - 1
        else:
            return result
