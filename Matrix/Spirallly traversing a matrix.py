#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        top =0
        down=r-1
        l=0
        r=c-1
        dirr=0
        ans=[]
        
        while(top<=down and l<=r):
            if(dirr==0):
                for i in range(l,r+1):
                    ans.append(matrix[top][i])
                top+=1
            elif (dirr==1):
                for i in range(top,down+1):
                    ans.append(matrix[i][r])
                r-=1
            elif(dirr==2):
                for i in range(r,l-1,-1):
                    ans.append(matrix[down][i])
                down-=1
            elif(dirr==3):
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][l])
                l+=1       
            dirr=(dirr+1)%4           
        return ans