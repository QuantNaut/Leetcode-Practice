def searchMatrix(matrix, target):
    for row in matrix:
        row_size = len(row) - 1
        left_ptr = 0
        right_ptr = row_size
    
        # Start search
        if target >= row[left_ptr] and target <= row[right_ptr]:
            while left_ptr <= right_ptr:
                mid_pt = (left_ptr + right_ptr) // 2
                
                if row[mid_pt] == target:
                    return True
                if target > row[mid_pt]:
                    left_ptr = mid_pt + 1
                else:
                    right_ptr = mid_pt - 1
                
                # No match found. Return false
                if left_ptr > right_ptr:
                    return False
    # No match found. Return false
    return False

def main():
    # Open and read from input file
    file = open('input.txt', 'r') # Swap out name of the different input files as you like here
    target = int(file.readline()) # Read the target number
    matrix = []
    for line in file: # Read the 2D matrix
        matrix.append([int(num) for num in line.split(' ')])
    
    print(searchMatrix(matrix, target))
    
# Run the program
if __name__ == '__main__':
    main()
