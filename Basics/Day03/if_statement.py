age = int(input("나이를 입력하세요 : "))    # input은 입력을 문자열(string)으로 받는다. 나이는 숫자로 비교해야 하므로 int() 함수를 사용한다.
if age >= 20:
    print("성인입니다.")    # Python은 들여쓰기(Indentation) 문법이다.
else:
    print("미성년자입니다.")