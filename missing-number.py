# Missing Number
# 
"""
Given an array nums containing n distinct numbers in the range [0, n] return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only o(1) extra space complexity and O(n) runtime complexity?
"""
# O(1) will need some binary properties
# XOR operator is required or "exclusive-or" operator.
# Lets say we wanna 2 ^ 3 (^ is the symbol for XOR)
# bit reps of each     1 0
#                      1 1
# If they're different:  1
# Otherwise we get:      0

# Example:
# input: [3, 0, 1]
# range = len(input)
# range = [0, 3]
# now we can 
# [3,0,1] ^ [0,1,2,3]

# While I thought this was a pretty greate solution, these were the results:
# Runtime: 250 ms, faster than 20.65% of Python3 online submissions for Missing Number.
# Memory Usage: 15.5 MB, less than 51.46% of Python3 online submissions for Missing Number.
# Let's see if we can get better numbers than that.

def missingNumber1(nums):
    return sum(range((len(nums)+1))) - sum(nums)

# From a youtube video, https://www.youtube.com/watch?v=WnPLSRLSANE&ab_channel=NeetCode
# It kind of took me a little while to wrap my head around it.
    # You can start with the length of the input array
    # as the response because the for loop will be adding (or subtracting in the case of negatives)
    # to that value.
def missingNumber2(nums):
    res = len(nums)
    print(f"The original response is: {res}")
    print("For each number in the range, we will add the difference between")
    print("the index number and the value of that index from the original list")
    print("to get our desired result.")
    print("Incrementally it looks like")
    for i in range(len(nums)):
        print(f"When we substract nums[i]: {nums[i]} from i: {i} we get: {(i-nums[i])}")
        print(f"We now add the result of that value {(i-nums[i])} to {res}")
        res += (i - nums[i])
        print(f"The incremental result of the for loop is: {res}")
    print(f"The end result is: {res}")

# To be honest, I'm still not entirely certain why that works out the way it does..
# We got another good one from the youtube comments:

def missingNumber3(nums):
    n = len(nums)
    print(n)
    res = 0.5 * n
    print(f"We are apparently halving n here: {res}")
    res = res * (n+1)
    print("Here, we multiply half of the length of the list by the length + 1 (to get the true range)")
    print(f"of the list to get {res}")
    s = sum(nums)
    print(f"Then we get the sum of the numbers in the list which is: {s}")
    res = res - s
    print(f"Then we subtract the sum of the list by whatever value we got for res before.. to get:")
    print(int(res))
    #res = 0.5*n*(n+1) - sum(nums) 
    #return int(res)

def main():
    