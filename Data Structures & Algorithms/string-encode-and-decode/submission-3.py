class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        #Entirely new approach 
        #Let the encoding be like 
        # 5#hello5#world

        # Build the total string first 
        for word in strs:
            # Get the length of the word. 
            individual_string_length = len(word)
            encoded_string += str(individual_string_length) + "#"

            #Now, for each character in that word
            for c in word:
                encoded_string += c
        
        print("First Print:", encoded_string)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = list()

        tmp_str = ""

        word_length = "" 

        i = 0

        while i < (len(s)):

            word_length = ""

            while(s[i] != "#"):
                word_length += s[i]
                i = i+1
            
            word_length = int(word_length)

            i += 1

            tmp_str = s[i: i + word_length]

            decoded_strs.append(tmp_str)

            i += word_length

        return decoded_strs
