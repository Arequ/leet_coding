nums = [-1,0,3,5,9,12]
target = 9
class Solution:
    def search(self, nums, target):
        """
        sortedNums = sorted(nums)
        while len(sortedNums):
            half = round(len(sortedNums)/2)
            if sortedNums[half] == target:
                print(half)
                return nums.index(half)
            elif sortedNums[half] > target:
                sortedNums = sortedNums[:half]
            elif sortedNums[half] < target:
                sortedNums = sortedNums[half:]
        """
        return nums.index(target)
                
print(Solution().search(nums, target))