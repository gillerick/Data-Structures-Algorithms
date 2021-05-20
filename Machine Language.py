# %%
def solution(S: str):
    operations = S.split(' ')
    stack = []
    for operation in operations:
        if operation == 'POP':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(-1)
                break
        elif operation == 'DUP':
            if len(stack) > 0:
                stack.append(stack[len(stack)-1])
            else:
                stack.append(-1)
                break
        elif operation == '+':
            if len(stack) > 1:
                try:
                    num_1 = int(stack.pop())
                    num_2 = int(stack.pop())
                    stack.append(num_1+num_2)
                except ValueError:
                    stack.append(-1)
                    break
            else:
                stack.append(-1)
                break
        elif operation == '-':
            if len(stack) > 1:
                try:
                    num_1 = int(stack.pop())
                    num_2 = int(stack.pop())
                    stack.append(num_1-num_2)
                except ValueError:
                    stack.append(-1)
                    break
            else:
                stack.append(-1)
                break
        else:
            try:
                num = int(operation)
                stack.append(num)
            except ValueError:
                stack.append(-1)
                break
    if len(stack) > 0:
        return stack[len(stack)-1]
    else:
        return -1

# %%
print(solution('4 5 6 - 7 +'))
print(solution('13 DUP 4 POP 5 DUP + DUP + -'))
print(solution('5 6 + -'))
print(solution('3 DUP 5 - -'))
# %%
