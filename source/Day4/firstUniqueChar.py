# Worst Case: O(n*log(n))
def firstUniqChar(s):
    # hash storage
    storage = dict()
    gen = list()
    for i in range(len(s)):
        count = 0
        index = i
        if s[i] not in storage:
            pair = list()
            # char as key, (index, count) as value in storage
            storage[s[i]] = pair
            pair.append(index)
            pair.append(count+1)
        elif s[i] in storage:
            storage[s[i]][1] = storage[s[i]][1] + 1
    # return the lowest index
    for value in storage.values():
        gen.append(value)
    if len(gen) != 0:
        gen.sort()
        current = gen[0]
        currentMin = gen[0][1]
        currentIndex = gen[0][0]
        for i in range(1, len(gen)):
            if gen[i][1] < currentMin:
                currentMin = gen[i][1]
                currentIndex = gen[i][0]
                current = gen[i]
        if current[1] > 1:
            return -1
        else:
            return currentIndex
    else:
        return -1

s = "loveleetcode"
print(firstUniqChar(s))

# Worst Case: O(n)
def firstUniqCharOpt(s):
    # hash storage
    storage = dict()
    for i in range(len(s)):
        count = 0
        if s[i] not in storage:
            storage[s[i]] = count + 1
        else:
            storage[s[i]] += 1
    # check for first unique
    for i in range(len(s)):
        if storage[s[i]] == 1:
            return i
    return -1

s = ""
print(firstUniqCharOpt(s))
