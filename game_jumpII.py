nums = [2,3,1,1,4]
 #     [0,1,2,3,4]

def jump_game(nums):

    jump = 0 
    current_end = 0 
    furthest = 0 

    for i in range(len(nums)-1):
        furthest = max(furthest,nums[i]+i)
        if i == current_end:
            jump+=1 
            current_end = furthest
            if current_end >= len(nums)-1:
                break 
    return jump

print(jump_game(nums))


        


