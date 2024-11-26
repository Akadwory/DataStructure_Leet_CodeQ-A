nums = [1,2,3,4,5,6,7]
nums_reversed = [4,5,6,7,1,2,3]
k = 4
n = len(nums)

def rotate(nums,k):
    n = len(nums)
    k = k % n 
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

    return nums

print(rotate(nums,k))
