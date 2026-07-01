# 함수 : 자주 사용하는 코드를 이름 붙여서 저장하는 것
def printParagraph() :
    print()
    print()
    print()


def greeting():
    print("안녕하세요")

greeting()
greeting()
greeting()

printParagraph()

def greeting2():
    print("안녕하세요!")
    print("AI Bootcamp를 준비 중입니다.")

greeting2()

printParagraph()

def greeting3(name):
    print(name, "님 안녕하세요!")

greeting3("최민정")

printParagraph()

def introduce(name, dream):
    print("안녕하세요.")
    print("제 이름은", name, "입니다.")
    print("제 목표는", dream, "입니다.")

introduce("최민정", "AI Engineer")

printParagraph()

# return : 함수의 결과를 반환하는 것
def add(a, b):
    return a + b

result = add(3, 5)
print("result : ", result)