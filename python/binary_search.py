

def binarysearch(nums, target):
    return bshelper(nums, target, 0, len(nums)-1)


def bshelper(nums, target, start, end):
    if start > end: return False 

    mid = start + (end-start) // 2

    if nums[mid] == target:
        return True
    elif target > nums[mid]:
        return bshelper(nums, target, mid+1, end)
    else:
        return bshelper(nums, target, start, mid-1)



ans = -1
def lowerbound(nums, target):
    global ans
    lowerboundhelper(nums, target, 0, len(nums)-1)
    return ans

def lowerboundhelper(nums, target, start, end):
    global ans
    if start > end: return start

    mid = start + (end-start) // 2

    if nums[mid] < target:
        return lowerboundhelper(nums, target, mid+1, end)
    else:
        ans = mid
        return lowerboundhelper(nums, target, start, mid-1)


ans2 = -1 
def upperbound(nums, target):
    global ans2
    ans2 = len(nums)
    upperboundhelper(nums, target, 0, len(nums)-1)
    return ans2

def upperboundhelper(nums, target, start, end):
    global ans2
    if start > end: return start

    mid = start + (end-start) // 2

    if nums[mid] <= target:
        return upperboundhelper(nums, target, mid+1, end)
    else:
        ans2 = mid
        return upperboundhelper(nums, target, start, mid-1)


def frequency(nums, target):
    lowerbound_position = lowerbound(nums, target)
    upperbound_position = upperbound(nums, target)
    if lowerbound_position == -1: return 0
    return upperbound_position - lowerbound_position






   # 0 1 2 3 4 5 6 7 8 9
a = [1,1,1,2,2,3,3,5,5,5]
target = 5
print(frequency(a, target))