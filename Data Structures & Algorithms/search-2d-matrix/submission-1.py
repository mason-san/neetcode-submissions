class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first identify the row in which the number might fall 
        start_row = 0 
        end_row = len(matrix) - 1

        while start_row <= end_row:
            mid_row_val = (start_row + end_row) // 2
        

            if target >= matrix[mid_row_val][0] and target <= matrix[mid_row_val][-1] :
                start_col = 0 
                end_col = len(matrix[0]) - 1

                while start_col <= end_col: 
                    mid_col = (start_col + end_col) // 2
                    if target == matrix[mid_row_val][mid_col]:
                        return True
                    
                    elif target < matrix[mid_row_val][mid_col]:
                        end_col = mid_col - 1
                    
                    else:
                        start_col = mid_col + 1
                
                return False

            elif target < matrix[mid_row_val][0]:
                end_row = mid_row_val - 1
            
            else: 
                start_row = mid_row_val + 1
                
        return False


        