def f(array):
    
    min_number = float('inf')
    min_row = -1
    min_col = -1
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            current_num = array[i][j]
            
            if current_num < min_number:
                min_number = current_num
                min_row = i
                min_col = j
                
    return min_row == min_col

if __name__ == "__main__":
    # Test cases from the exam sheet
    # Smallest is 3 at row 1, col 1 -> True
    print(f([[7,8],[5,3],[9,4]])) 
    
    # Smallest is 2 at row 1, col 2 -> False
    print(f([[7,8,5,3], [9,4,2,6]]))