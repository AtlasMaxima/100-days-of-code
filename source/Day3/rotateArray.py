'''Rotate 1-D Array'''

# Worse Case: O(n)
def rotate(input, k):
    i = 0
    while i < k:
        lastVal = input[-1]
        firstVal = input[0]
        # replace first element with lastVal
        input.insert(0,lastVal)
        # delete the last element
        del input[len(input) - 1]
        i += 1
    print(input)

k = 3
arr1 = [1,2,3,4,5,6,7]
rotate(arr1, k)
