nums = [int(i) for i in input().split()]
target = int(input())
nums.sort()


def binary_search(arr, low, high, x):
     
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

print(binary_search([3, 2, 4], 1, 2, 3))

exit()
for i in range(len(nums)):
    res = binary_search(nums, i, len(nums), target-nums[i])
    # print("["+str(i)+","+str(res)+"]")
    if res!=-1:
        print(i, res)
        # print("["+str(i)+","+str(res)+"]")
        break