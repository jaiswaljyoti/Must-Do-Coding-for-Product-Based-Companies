#User function Template for python3

def rotate(matrix): 
    #code here
    for i in range(len(matrix)):
        matrix[i].reverse()
 
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]