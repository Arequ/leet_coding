"""
Given an array of integers nums sorted in non-decreasing 
order, find the starting and ending position of a given 
target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return [-1, -1]
        first = nums.index(target)
        last = (len(nums) - 1) - nums[::-1].index(target)
        return [first, last]

examples = [
    [ [ 5,7,7,8,8,10 ], 8 ],
    [ [ 5,7,7,8,8,10 ], 6 ],
    [ [ ], 0 ]
    ]
s = Solution()
for example in examples:
    print( s.searchRange( example[0], example[1] ) )
        