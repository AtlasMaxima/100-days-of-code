'''
binary = [128, 64, 32, 16, 8, 4, 2, 1]
num1 = 5 #0101
num2 = 3 #0011
num1 + num2 = output #0111
output = 8 #1000
'''

def int2Binary(num):
    output = [0] * 8
    current = num
    binary = [128, 64, 32, 16, 8, 4, 2, 1]
    # Find the largest number that num can subtract - loop
    for i in range(len(binary)):
        # If the num - binary[i] < 0, place a 0
        if current - binary[i] < 0:
            output[i] = 0
        # If the num - binary[i] > 0, then place a 1 in the output array
        elif current - binary[i] > 0:
            output[i] = 1
            current = current - binary[i]
        elif current - binary[i] == 0:
            output[i] = 1
            current = current - binary[i]
    # If the num - binary[i] == 0, return output
    print(output)

num = 50
print(int2Binary(num))
