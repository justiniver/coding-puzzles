class Solution:
    def __isLeftParen(self, c: str) -> bool:
        return c == "(" or c == "{" or c == "["
    
    def __parenConverter(self, c: str) -> str:
        if c == ")":
            return "("
        elif c == "}":
            return "{"
        else:
            return "["
        return "error"

    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            if self.__isLeftParen(s[i]):
                stack.append(s[i])
            else:
                if self.__parenConverter(s[i]) != stack[-1]:
                    return False
                
                stack.pop()

        return len(stack) == 0
        