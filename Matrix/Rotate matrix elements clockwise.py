#User function Template for python3

class Solution:
    def rotateMatrix(self, M, N, Mat):
        #code here
        if not len(Mat):
            return
    
        top = 0
        bottom = M-1
        left = 0
        right = N-1
     
        while left < right and top < bottom:
            prev = Mat[top+1][left]
            for i in range(left, right+1):
                curr = Mat[top][i]
                Mat[top][i] = prev
                prev = curr
     
            top += 1
            for i in range(top, bottom+1):
                curr = Mat[i][right]
                Mat[i][right] = prev
                prev = curr
     
            right -= 1
            for i in range(right, left-1, -1):
                curr = Mat[bottom][i]
                Mat[bottom][i] = prev
                prev = curr
     
            bottom -= 1
            for i in range(bottom, top-1, -1):
                curr = Mat[i][left]
                Mat[i][left] = prev
                prev = curr
 
            left += 1
            
        return Mat