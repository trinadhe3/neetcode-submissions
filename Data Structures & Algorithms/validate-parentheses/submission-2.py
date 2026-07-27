class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            "}" : "{",
            "]" : "[",
            ")" : "("

        }
        for curr in s:
            if curr == "(" or curr == "{" or curr == "[":
                stack.append(curr)
            else:
                if not stack or check[curr] != stack[-1]:
                    return False
                stack.pop()
        return stack == []