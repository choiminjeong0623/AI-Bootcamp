answer = 7
number = int(input("숫자를 입력하세요 (1~10):"))

print("==== 예제01 ====")
if(number == answer):
    print("정답입니다!")
else:
    print("틀렸습니다. 정답은 ", answer, "입니다.")
print()
print()
print("==== 예제02 ====")
if(number < answer):
    print("더 큰 숫자입니다.")
elif(number > answer):
    print("더 작은 숫자입니다.")
elif(number == answer):
    print("정답입니다!")