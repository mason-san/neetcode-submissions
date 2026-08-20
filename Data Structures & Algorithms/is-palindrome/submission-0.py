class Solution:
    def isPalindrome(self, s: str) -> bool:

        #clean string
        clean_str = "".join(c for c in s if c.isalnum())

        #get the legnth of the string. 
        n = len(clean_str)

        #i just need to do the two pointer technique
        # and if i see that any of them is not true
        #return false
        start = 0
        end = (n - 1)

        print(clean_str)

        #loop infinitely
        while start < end:
            if clean_str[start].lower() != clean_str[end].lower():
                return False
            
            start+= 1
            end -= 1

        return True




        