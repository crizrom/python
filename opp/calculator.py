class Calculator: 
    def __init__(self, n1, n2):
        self.sum = n1 + n2
        self.minus = n1 - n2
        self.division = n1 / n2
        self.multiply = n1 * n2

print('***********Welcome to the test calculator!!!***********')
print('This is just a test, this calculator uses float numbers')

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a second number: '))
operation = Calculator(num1, num2)

print(operation.sum)
print(operation.minus)
print(operation.division)
print(operation.multiply)