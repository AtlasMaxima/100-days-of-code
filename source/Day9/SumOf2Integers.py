'''
a = 1 #0001
b = 2 #0010
c = 3 #0011

a & b = 0 #0000
a ^ b = 3 #0011
a | b = 3 #0011
a + b = 3 #0011

b ^ c = 1 #0001
b & c = 2 #0010
b + c = 5 #0101
0101
0001
0101
'''

def getSumShift(num1, num2):
    while(num2):
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1
print(getSumShift(1, 1))

def getSumPlus(a, b):
    sum = a ^ b
    carry = (a & b) << 1
    # add the sum and the carry bits
    sum += carry
    return sum

print(getSumPlus(12, 25))
