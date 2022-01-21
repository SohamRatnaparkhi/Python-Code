
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    start = nums[mid:]
    end = nums[:mid]

    start, end = merge_sort(start), merge_sort(end)

    return merge(start, end)
def merge(start, end):
    merged = []

    i, j = 0, 0

    while(i < len(start) and j < len(end)):
        if start[i] < end[j]:
            merged.append(start[i])
            i += 1

        else:
            merged.append(end[j])
            j += 1

    return merged + start[i:] + end[j:]

print(merge_sort([2, 43, 12, 123, 123, 134, 100, 43, 21]))