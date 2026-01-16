def f(array2D):
    
    size = len(array2D)
    
    for i in range(size):
        row_sum = 0
        for num in array2D[i]:
            row_sum += num
            
        col_sum = 0
        for j in range(size):
            col_sum += array2D[j][i]
            
        if row_sum != col_sum:
            return False
        
    return True

if __name__ == "__main__":
    # Test cases from the exam sheet
    print(f([[3,7,2], [4,2,5], [9,2,1]])) # Should be False [cite: 30]