class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        d=dict()
        result=[]
        for index,element in enumerate(nums):
            d[element]=index
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                target=0-nums[i]-nums[j]
                if target in d and d[target]>j:
                    result.append([nums[i],nums[j],target])
        return result
