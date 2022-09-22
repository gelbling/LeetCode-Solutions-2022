
nums_original = [-1,0,3,5,9,12]
nums = [-1,0,3,5,9,12]

target = 9

found = False
        
while found != True:

    if len(nums) == 1 or 0:
        print('-1')
        break

    sz = int((len(nums))/2)

    if nums[sz] > target:
        nums = nums[:sz]
    elif nums[sz] == target:
        print(nums_original.index(target))
        found = True
    else:
        nums = nums[sz:]


