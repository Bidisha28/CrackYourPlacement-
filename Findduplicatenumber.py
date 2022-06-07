class Solution(object):
    def findDuplicate(self, nums):
        l={}
        for i in nums:
            if i not in l:
                l[i]=1
            else:
                return i