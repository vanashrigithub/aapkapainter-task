

#Program to prints out the first occurrence of a duplicate
# in a given array of integers

def find_first_duplicate(nums):
    num_set=set()
    first_duplicate=-1
    for i in range(len(nums)):
        if nums[i] in num_set:
            return nums[i]
        else:
            num_set.add((nums[i]))
    return first_duplicate
print(find_first_duplicate([1,2,3,2,1]))