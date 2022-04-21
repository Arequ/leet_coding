def containsDuplicate(nums):
    """
    Parameters:
    nums (list): a list of numbers with potential duplicates.
    Returns:
    boolean: whether or not a duplicate is present.
    """
    return len(set(nums)) != len(nums)

tests = [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True)
]

for nums, exp_out in tests:
    output = containsDuplicate(nums)
    print(output)
    if output == exp_out:
        print(f"Input: {nums}, Expected: {exp_out}, Output: {output}, Result: Passed.")
    else:
        print(f"Input: {nums}, Expected: {exp_out}, Output: {output}, Result: Failed")

