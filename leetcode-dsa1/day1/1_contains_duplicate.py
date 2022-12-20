def containsDuplicate(nums):
    for i in range(0, len(nums)):
        key = nums[i]
        for j in range(i+1, len(nums)):
            if key == nums[j]:
                return True
    return False