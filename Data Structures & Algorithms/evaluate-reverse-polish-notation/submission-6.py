class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        #for each character in tokens 
        for each_token in tokens:
            #add the number to the stack 
            if each_token not in ['+', '-', '*', '/']:
                stack.append(int(each_token))
            else:
                if len(stack) > 0:
                    n1 = int(stack.pop())
                    n2 = int(stack.pop())

                res = 0

                match each_token:
                    case '+':
                        res = int(n1 + n2)
                        stack.append(res)
                    case '-':
                        res = n2 - n1
                        stack.append(res)
                    case '*':
                        res = n1 * n2
                        stack.append(res)
                    case '/':
                        res = int(n2 / n1)
                        stack.append(res)

            # print(stack)

        return int(stack[-1])


        