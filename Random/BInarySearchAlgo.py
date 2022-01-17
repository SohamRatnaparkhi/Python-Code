def BinarySearchAsc(l, target):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in ascending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    
    s = 0
    e = len(l) - 1

    while(s <= e):
        mid = int(s + (e - s) / 2)
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            e = mid - 1
        elif l[mid] < target:
            s = mid + 1
        else:
            return -1
        
def BinarySearchDesc(l, target):
    """Searches a target element in array using binary search algorithm

    Args:
        l ([list]): [Array sorted in descending order]
        target ([int]): [element to be searched]

    Returns:
        [integer]: [index of target element if it is found else - 1]
    """
    s = 0
    e = len(l) - 1 

    while s <= e:
        mid = int(s + (e - s) / 2)
        
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            s = mid + 1
        elif l[mid] < target:
            e = mid - 1
        else:
            return -1

print(BinarySearchDesc([10,9,8,7,6,5,4,3,2,1,0], 2))