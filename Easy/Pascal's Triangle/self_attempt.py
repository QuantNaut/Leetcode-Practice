def generate(numRows):
    # Return these outputs if given num is 1 or 2
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    
    # Initialize triangle with initial 2 rows
    triangle = [[1], [1,1]]
    
    # Create and add the new rows
    for i in range(2, numRows): # Ignore the first 2 rows
        newRow = [] # New row to be added
        
        # Get the previous row
        prevRow = triangle[i-1]
        prevRowSize = len(prevRow)
        left_n, right_n = prevRow[0], prevRow[prevRowSize-1] # Get leftmost and rightmost nums
        left, right = 0, 1 # Left and right pointers
        
        # Calculate the numbers
        newRow.append(left_n)
        for j in range(prevRowSize-1):
            num = prevRow[left] + prevRow[right]
            newRow.append(num)
            left += 1
            right += 1
        newRow.append(right_n)
        
        # Add the new row 
        triangle.append(newRow)
    
    # Return the result
    return triangle

def main():
    n = int(input('Enter number of rows: '))
    while n < 1 or n > 30:
        print('Number input should be between the range of 1 and 30 (inclusive)')
        n = int(input('Enter number of rows: '))
    print(generate(n))
    
# Run the program
if __name__ == '__main__':
    main()
