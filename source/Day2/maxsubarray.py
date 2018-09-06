# Worst Case: O(n)
def kadane(input):
    max_current = max_global = input[0]
    for i in range(1, len(input)):
        max_current = max(input[i], max_current + input[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

print(kadane([-2,1]))
