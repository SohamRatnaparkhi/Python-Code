def find_pivot(nums):
    s = 0
    e = len(nums) - 1
    mid = int((s + e) / 2) 
    while s < e:
        mid = int((s + e) / 2)
        if nums[mid] > nums[mid + 1] :
            e = mid
        elif nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
            if nums[mid + 1] > nums[mid - 1]:
                s = mid + 1
            else:
                e = mid - 1
        elif nums[mid] < nums[mid + 1]:
            s = mid + 1
        else:
            return (nums[mid], mid)
    return (nums[s], s)
    
def BinarySearchAsc(l, target, s, e):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in ascending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    

    while(s <= e):
        mid = int(s + (e - s) / 2)
        
        if l[mid] > target:
            e = mid - 1
        elif l[mid] < target:
            s = mid + 1
        else:
            
            return mid
    return -1

def BinarySearchDesc(l, target, s, e):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in descending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
     

    while s <= e:
        mid = int(s + (e - s) / 2)
            
        if l[mid] > target:
            s = mid + 1
        elif l[mid] < target:
            e = mid - 1
        else:
            return mid
    return -1

def Order_agnostic_BinarySearch(l, target, s, e):
    ans = 0
    if l[0] < l[1]: 
        # Ascneding order
        ans = BinarySearchAsc(l, target, s, e)
    else :
        # Descending order
        ans = BinarySearchDesc(l, target, s, e)
    return ans

def main():
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    x = (find_pivot(nums))
    (pivot, index) = (x[0], x[1])
    length = len(nums)
    left_ans = Order_agnostic_BinarySearch(nums, target, 0, index + 1)
    right_ans = 0
    if left_ans == -1:
        right_ans = Order_agnostic_BinarySearch(nums, target, index, length - 1) 
        print(right_ans)
    else:
        print(left_ans)

main()
