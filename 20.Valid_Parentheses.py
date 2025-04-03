class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if(char == '(' or char == '{' or char == '['):
                stack.append(char)
            elif(char == ')' or char == '}' or char == ']'):
                if stack:
                    if char == ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    elif char == '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                    elif char == ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False if stack else True          
                    