class Solution(object):
    def removeDuplicates(self, nums):
        #2-pointer-concept
        s,f=0,1
        if len(nums)==1:
            return 1
        while(f<len(nums)):
            if nums[s]==nums[f]:
                f+=1
            else:
                s+=1
                nums[s]=nums[f]
                f+=1
        return s+1