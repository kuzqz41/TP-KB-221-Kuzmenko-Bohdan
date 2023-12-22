def zpz(inp):
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
    return outp



def answ(outp):
    while len(outp) != 1:
        for i in range(len(outp)):
            if outp[i] == "*":
                outp [i-2] = float(outp [i-2]) * float(outp[i-1])
                outp.pop(i-1)
                outp.pop(i-1)
                break
            elif outp[i] == "/":
                outp [i-2] = float(outp [i-2]) / float(outp[i-1])
                outp.pop(i-1)
                outp.pop(i-1)
                break
            elif outp[i] == "+":
                outp [i-2] = float(outp [i-2]) + float(outp[i-1])
                outp.pop(i-1)
                outp.pop(i-1)
                break
            elif outp[i] == "-":
                outp [i-2] = float(outp [i-2]) - float(outp[i-1])
                outp.pop(i-1)
                outp.pop(i-1)
                break
            elif outp[i] == "^":
                outp [i-2] = float(outp [i-2]) ** float(outp[i-1])
                outp.pop(i-1)
                outp.pop(i-1)
                break
    return outp[0]


def main():
    inp = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
    print (' '.join(zpz(inp)), " = ", answ(zpz(inp)))


if __name__ == "__main__":
    main()