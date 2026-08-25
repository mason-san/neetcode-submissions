class Solution:
    def isValid(self, s: str) -> bool:

        #create a stack variable 
        stack = list() 

        brackets = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        #loop through the strings
        for c in s:
            if c in brackets.values():
                stack.append(c)
            
            else: 
                if not stack or stack[-1] != brackets[c]:
                    return False
                
                stack.pop()

        
        return len(stack) == 0



        