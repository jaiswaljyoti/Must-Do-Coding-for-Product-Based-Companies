
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack = []
        stack.append(0)
        for i in range(1,n):
            while stack and arr[stack[-1]]<arr[i]:
                index=stack.pop()
                arr[index]=arr[i]
            stack.append(i)
        while stack:
            index=stack.pop()
            arr[index]=-1
        return arr