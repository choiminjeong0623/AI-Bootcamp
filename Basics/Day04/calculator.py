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
        return a / b

def modulo(a, b):
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

resultModulo = modulo(num1, num2)
print("modulo 함수의 결과 : ", modulo(num1, num2))
