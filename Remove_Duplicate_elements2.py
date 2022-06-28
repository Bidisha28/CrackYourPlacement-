class Solution(object):
    def removeDuplicates(self, nums):
        #2 pointer concept
        c=1
        while(c<len(nums)-1):
            if nums[c]==nums[c-1] and nums[c]==nums[c+1]:
                del nums[c]
            else:
                c+=1
                
        return len(nums)