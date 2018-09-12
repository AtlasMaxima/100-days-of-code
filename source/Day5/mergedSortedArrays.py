# Worst Case: O(m+n)
def merge(nums1, m, nums2, n):
    # if nums1 is empty
    if m == 0:
        for i in range(0, n):
            nums1 = [nums2[i] for i in range(0, n)]
        return nums1
    # setting up the three pointers
    mergeIndex = m + n - 1
    indexA = m - 1
    indexB = n - 1
    while indexA >= 0 and indexB >= 0:
        if nums1[indexA] > nums2[indexB]:
            # copy nums1[indexA] to nums1[index]
            nums1[mergeIndex] = nums1[indexA]
            indexA -= 1
            mergeIndex -= 1
        else:
            nums1[mergeIndex] = nums2[indexB]
            indexB -= 1
            mergeIndex -= 1
    # to make sure it will still copy over once indexA reaches -1
    while indexB >= 0:
        nums1[mergeIndex] = nums2[indexB]
        indexB -= 1
        mergeIndex -= 1
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1, 3, nums2, 3))

# Worst Case: O(nlogn) of Tim Sort 
# Using the sort method in Python
def mergeSort(nums1, m, nums2, n):
    # replace nums1 elements with nums2
    for i in range(len(nums2)):
        nums1[m] = nums2[i]
        m += 1
        if m == len(nums1):
            break
    return nums1.sort()
