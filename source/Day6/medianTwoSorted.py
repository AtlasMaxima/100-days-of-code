# Worst Case: O(n log n + m)
def naive(A, B):
    C = A + B # O(m + n)
    C.sort() # O(n log n)
    m = len(C)
    median = 0
    if m % 2 == 0: # C array has an even length
        index1 = m / 2
        index2 = index1 - 1
        median = (C[index1] + C[index2]) / float(2)
    else: # C array has an odd length
        median = m / 2
    return median

A = [1,2]
B = [1,3,6,7]
naive(A,B)

#Worst Case: O(n1 + n2) => O(n)
def linear(A, B):
    C = [0] * (len(A) + len(B))
    indexA = 0
    indexB = 0
    indexC = 0
    median = 0
    while indexA < len(A) and indexB < len(B):
        # compare values at indexA and indexB
        if A[indexA] < B[indexB]:
            # place A[indexA] in C[index]
            C[indexC] = A[indexA]
            # increment indexA
            indexA += 1
        else:
            C[indexC] = B[indexB]
            # increment indexB
            indexB += 1
        indexC += 1
    # if indexA has reached the end yet indexB still remains
    while indexB < len(B):
        # append everything into C
        C[indexC] = B[indexB]
        indexB += 1
        indexC += 1
    m = len(C)
    if m % 2 == 0: # C array has an even length
        index1 = m / 2
        index2 = index1 - 1
        median = (C[index1] + C[index2]) / float(2)
    else: # C array has an odd length
        median = m / 2
    return median


print(linear(A,B))
