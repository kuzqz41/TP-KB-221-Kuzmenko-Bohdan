inp = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

outp = []
stack = []

for i in inp.split():
    if i.isnumeric():
        outp.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack[len(stack)-1] != '(':
            outp.append(stack.pop())
        stack.pop()
    elif i in priority:
        while stack and priority[stack[len(stack)-1]] >= priority[i]:
            outp.append(stack.pop())
        stack.append(i)

while stack:
    outp.append(stack.pop())
    
print (' '.join(outp))