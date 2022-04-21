## This is an example of dynamic programming which basically breaks
## a problem into smaller problems.

## tl;dr is: you keep track of the maximum sum and iterate through the list just once
## the algo checks to see if the current number by itself is greater than the entire
## sum of the last subarray. At that point it is fair to say that the sum of any list created
## by the number in the current index and possibly to the right will by default be bigger 
## than the stuff on the left.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        last_max_sum = 0
        for i in range(len(nums)):
            if nums[i] > nums[i] + last_max_sum:
                last_max_sum = nums[i]
            else:
                last_max_sum = nums[i] + last_max_sum
            if last_max_sum > max_sum:
                max_sum = last_max_sum
        return max_sum


s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums1 = [-2,1]
print(f"Output: {s.maxSubArray(nums)}")
print("Expected: 6")
print(f"Output: {s.maxSubArray(nums1)}")
print("Expected: 1")

"""
max_sum = -999999999999999999999999999999999999999999
[-2] = last_max_sum = -2 > max_sum so last_max_sum is now -2
[-2, 1] = last_max_sum = -1 > max_sum so last_max_sum is now -1
[1] = last_max_sum = 1 > max_sum so last_max_sum is now 1
return 1
"""