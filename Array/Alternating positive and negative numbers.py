#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        l1 = []
        l2 = []
        for element in arr:
            if element<0:
                l2.append(element)
            else:
                l1.append(element)
        i =0
        j = 0
        k = 0
    
        while(i<len(l1) and j<len(l2)):
            if(k%2==0):
                arr[k] = l1[i]
                i+=1
                
            else:
                arr[k] = l2[j]
                j+=1
            k+=1
            
        while(i<len(l1) and k<n):
            arr[k] = l1[i]
            k+=1
            i+=1
        while(j<len(l2) and k<n):
            arr[k] = l2[j]
            j+=1
            k+=1