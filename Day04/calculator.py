def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    else:
        return int(a / b)

def modular(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    else :
        return a % b
def exponent(a, b):
    return a ** b

num1 = int(input("첫 번째 숫자 : "))
num2 = int(input("두 번째 숫자 : "))

resultAdd = add(num1, num2)
print("add 함수의 결과 : ", resultAdd)

resultSubstr = substract(num1, num2)
print("substract 함수의 결과 : ", substract(num1, num2))

resultMultiply = multiply(num1, num2)
print("multiply 함수의 결과 : ", multiply(num1, num2))

ressultDivide = divide(num1, num2)
print("divide 함수의 결과 : ", divide(num1, num2))

resultModular = modular(num1, num2)
print("modular 함수의 결과 : ", modular(num1, num2))
