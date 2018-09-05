# Worse Case: O(n)
def isValid(s):
    a=['()','[]','{}']
    stack=""
    for i in s:
        if stack!='' and stack[-1]+i in a:
            stack=stack[:-1]
        else:
            stack+=i
    return stack==""


string = "(([]){})"
print(isValid(string))
