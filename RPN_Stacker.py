


if __name__ == "__main__":
    stk = []
    with open('./Calc1.stk') as file:
        for line in file:
            token = line.strip()
            if token.isdigit():
                stk.append(int(token))
            elif token in ['+', '-', '*', '/']:
                if len(stk) < 2:
                    raise ValueError("Not enough operands for operator " + token)
                operand_2 = stk.pop()
                operand_1 = stk.pop()
                if token == '+':
                    stk.append(operand_1 + operand_2)
                elif token == '-':
                    stk.append(operand_1 - operand_2)
                elif token == '*':
                    stk.append(operand_1 * operand_2)
                elif token == '/':
                    if(operand_2 == 0):
                        raise ZeroDivisionError("Error: Division by zero")
                    stk.append(operand_1 / operand_2)
            else:
                raise ValueError("Invalid Input " + token)
        if len(stk) != 1:
            raise ValueError("Invalid RPN File")
        print(stk.pop())
        
            

