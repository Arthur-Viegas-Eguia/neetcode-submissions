class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == "(" or symbol == "[" or symbol == "{":
                stack.append(symbol)
                continue
            if len(stack) >= 1 and ((symbol == ")" and stack[-1] == "(") or (symbol == "]" and stack[-1] == "[") or (symbol == "}" and stack[-1] == "{")):
                stack.pop()
            else:
                return False
        return len(stack) == 0