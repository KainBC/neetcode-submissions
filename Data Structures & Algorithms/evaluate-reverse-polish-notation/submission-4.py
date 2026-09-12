class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        for tok in tokens:
            if tok in ops:
                a = stack.pop()
                b = stack.pop()
                if tok == "+":
                    b += a
                elif tok == "-":
                    b -= a
                elif tok == "*":
                    b *= a
                else:
                    b = int(b / a)

                stack.append(b)
            else:
                stack.append(int(tok))

        return int(stack[0])