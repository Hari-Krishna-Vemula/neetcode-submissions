

class Solution:
    def twoSum(nums: List[int], target: int):
        res = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # avoid duplicates
                if nums[i] + nums[j] == target:
                    res.append([i, j])

        return res

print(Solution.twoSum([4, 5, 6, 5], 10))
