def merge(nums1, m, nums2, n):
    nums1[0:m+n] = sorted(nums1[:m]+nums2[:n])
    return nums1