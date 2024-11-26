nums = [3,0,0,0,4]



def game_jump(nums):
    goal = len(nums)-1 
    for i in range(len(nums)-1,-1,-1):
        if nums[i] + i >= goal:
            goal = i 
    return True if goal==0 else False

print(game_jump(nums))


