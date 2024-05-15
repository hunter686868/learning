from stack import Stack

def calculation(eq):
    stack2 = Stack()
    while eq[0] != '=':
        variable = eq.pop()
        if variable.isdigit():
            stack2.push(int(variable))
        elif variable == '+':
            rslt = stack2.pop() + stack2.pop()
            stack2.push(rslt)
        elif variable == '*':
            rslt = stack2.pop() * stack2.pop()
            stack2.push(rslt)
    return stack2.pop()


stack1 = ['8', '2', '+', '5', '*', '9', '=']
result = calculation(stack1)
print("Результат вычисления:", result)

