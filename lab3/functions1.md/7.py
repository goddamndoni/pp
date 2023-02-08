def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == nums[i+1] == 3):
            return True
    return False
a = list(map(int,input().split()))
print(has_33(a))