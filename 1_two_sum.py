class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            if sum(nums) == target:
                return [0,1]
        found = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in found:
                return i, found[diff]
            else:
                found[val] = i       