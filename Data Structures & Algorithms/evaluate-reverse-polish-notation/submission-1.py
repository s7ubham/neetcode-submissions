class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i == "+":
                ans = stack[-2] + stack [-1]
                stack=stack[:-2]
                stack.append(ans)
            elif i == "-":
                ans = stack[-2] - stack [-1]
                stack=stack[:-2]
                stack.append(ans)
            elif i == "*":
                ans = stack[-2] * stack [-1]
                stack=stack[:-2]
                stack.append(ans)
            elif i == "/":
                ans = stack[-2] / stack [-1]
                stack=stack[:-2]
                stack.append(int(ans))
            else:
                stack.append(int(i))
             
        return stack[0]
        