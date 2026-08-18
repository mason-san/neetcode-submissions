class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # so the input is a list of list 
        # would look something like 
        # [[1, 2, ., ., 3, ., ., ., .],
        #   [4, ., ., 5, ., ., ., ., ., .]]

        #rows would be 9
        #columns would be 9 
        #the board length would be 9
        # each element inside the board would be of length 9 

        #create three seperate list of sets 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        #so let's first loop through the board 
        for row in range(9):

            #now go through each of the values 
            for col in range(9):
                if (board[row][col].isnumeric()):
                    #to calculate the square that the value could be in 
                    horizontal_band = row//3
                    vertical_band = col//3
                    square_idx = (horizontal_band * 3) + vertical_band

                    #get the numeric value which is board[row][col]
                    #check if that value is in the board at index row 
                    if board[row][col] in rows[row]:
                        #duplicate 
                        return False
                    #Do the same for columns 
                    elif board[row][col] in cols[col]:
                        #duplicate
                        return False
                    #Now, check if it is in the 3x3 square. 
                    elif board[row][col] in squares[square_idx]:
                        #duplicate 
                        return False
            
                    #Even after going through, if i find that they are not there, 
                    # add them to the sets
                    #rows set 
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[square_idx].add(board[row][col])

        return True

        