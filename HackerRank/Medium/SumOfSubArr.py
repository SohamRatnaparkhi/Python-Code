nums = list(map(int, input().split(',')))
m = 0
if len(nums) == 1:
    print(nums[0])
else:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            s = sum(nums[i : j])
            if s > m:
                m = s
    print(m)