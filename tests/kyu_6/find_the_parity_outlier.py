def find_outlier(nums):
    parities = [n & 1 for n in nums]
    return nums[parities.index((parities[0] in parities[1:3]) ^ parities[0])]

