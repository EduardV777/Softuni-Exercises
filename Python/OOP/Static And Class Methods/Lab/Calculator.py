class Calculator:

    @staticmethod
    def add(*args):
        sum = [str(arg) for arg in args]
        sum = eval('+'.join(sum))
        return sum
    
    @staticmethod
    def multiply(*args):
        res = [str(arg) for arg in args]
        res = eval("*".join(res))
        return res
    
    @staticmethod
    def divide(*args):
        res = [str(arg) for arg in args]
        res = eval("/".join(res))
        return res

    @staticmethod
    def subtract(*args):
        res = [str(arg) for arg in args]
        res = eval('-'.join(res))
        return res



print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))