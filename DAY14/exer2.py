
def arrayCheck(nums):
    
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False
print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))