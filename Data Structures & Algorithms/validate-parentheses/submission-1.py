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
                if len(stack) == 0:
                    return False

                last_element = stack[-1]

                if last_element == brackets[c]:
                    stack.pop()
                else: 
                    return False

        
        if len(stack) == 0:
            return True
        return False



        