# try:
#     age = int(input("나이를 입력하세요 : "))
#     print("입력한 나이 : ", age)
# except:
#     print("숫자만 입력해주세요.")

try:
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))

    print("결과:", num1 / num2)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자만 입력해주세요.")