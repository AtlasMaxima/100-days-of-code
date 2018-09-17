# Worse Cast: O(n^2)
def binary2Int(num):
    # dictionary storage
    checker = {0: 1, 1: 2, 2: 4, 3: 8, 4: 16, 5: 32}
    # split the num into a list
    num = list(str(num))
    # reverse the num in the list
    num.reverse()
    total = 0

    for index in range(len(num)):
        if int(num[index]) == 1:
            # find the index in checker and sum total
            for key, value in checker.iteritems():
                if index == key:
                    total += value
    print(total)



binary2Int(111)
