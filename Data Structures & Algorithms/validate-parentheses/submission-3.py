class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p=="{" or p=="(" or p=="[":
                stack.append(p)
            else:
                if not stack:
                    return False
                out = stack.pop()
                if out=="{" and p=="}":
                    continue
                elif out=="(" and p==")":
                    continue
                elif out=="[" and p=="]":
                    continue
                else:
                    return False
            
        if not stack: return True
        else: return False