from stack import Stack

def calculation(eq):
    stack2 = Stack()
    while eq != '=':
        v = eq.pop()
        if v.isdigit():
            stack2.push(int(v))
        elif v == '+':
            rslt = stack2.pop() + stack2.pop()
            stack2.push(rslt)
        elif v == '*':
            rslt = stack2.pop() * stack2.pop()
            stack2.push(rslt)
    return stack2.pop()


stack1 = ['8', '2', '+', '5', '*', '9', '=']
result = calculation(stack1)
print("Результат вычисления:", result)

