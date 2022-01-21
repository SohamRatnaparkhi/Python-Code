def bs(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]

    return nums

print(bs([2, 43, 12, 123, 123, 134, 100, 43, 21]))
