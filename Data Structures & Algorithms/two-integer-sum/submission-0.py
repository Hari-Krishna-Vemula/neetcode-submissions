class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                try:
                    if i!=j and nums[i]+nums[j]==target:
                         out=[]
                         out.append(i)
                         out.append(j)
                         return out
                except:
                    pass