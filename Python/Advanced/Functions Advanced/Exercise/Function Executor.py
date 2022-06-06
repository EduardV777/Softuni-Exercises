def func_executor(*args):
    output=""
    for k in range(0,len(args)):
        functionName=str(args[k][0]); functionName=functionName.split(" "); functionName=functionName[1]
        functionCall=args[k][0]
        functionArguments=args[k][1]
        output+=f"{functionName} - {functionCall(*functionArguments)}\n"
    return output


def sum_numbers(num1, num2):

    return num1 + num2

def multiply_numbers(num1, num2):

    return num1 * num2

print(func_executor((sum_numbers, (1, 2)),(multiply_numbers, (2, 4))))