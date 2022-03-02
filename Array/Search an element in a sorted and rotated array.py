#User function Template for python3

def Search(arr,n,k):
    #code here
    l = 0
    r = n-1
    while(l<=r):
        mid = (l+r)//2
        if arr[mid]==k:
            return mid
        elif(arr[mid]>arr[l]):
            if(arr[mid]>=k and arr[l]<=k):
                r = mid-1
            else:
                l = mid+1
        else:
            if(arr[mid]<=k and arr[r]>=k):
                l = mid+1
            else:
                r = mid-1
        
    return -1