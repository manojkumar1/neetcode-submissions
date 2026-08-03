class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        
        for i in tokens:
            if i in ('+','-','*','/'):
                val1 = int(num_stack.pop())
                val2 = int(num_stack.pop())
                if i == '+':
                    val = val2 + val1
                if i == '-':
                    val = val2 - val1
                if i == '*':
                    val = val2 * val1
                if i == '/':
                    val = int(val2 / val1)
                num_stack.append(val)
            else:
                num_stack.append(int(i))

        return num_stack[-1]

            
        