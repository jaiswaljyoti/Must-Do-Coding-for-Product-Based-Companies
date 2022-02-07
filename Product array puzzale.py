
class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        pro = 1
        count = 0
        for num in nums:
            if(num!=0):
                pro*=num
            elif(num==0 and count==0):
                count+=1
            else:
                count+=1
                break
        for i in range(len(nums)):
            if(count>1):
                nums[i] = 0
            elif(nums[i] == 0):
                nums[i] = pro
            else:
                if(count>0):
                    nums[i] = 0
                else:
                    nums[i] = pro//nums[i]
        return nums