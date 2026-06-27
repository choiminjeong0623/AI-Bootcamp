import random

answer = random.randint(1, 10)

number = int(input("1~10 숫자를 입력하세요 : "))

if number == answer:
    print("정답입니다!")
else:
    print("틀렸습니다.")
    print("정답은 ", answer, "였습니다.")