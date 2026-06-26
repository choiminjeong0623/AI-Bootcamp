# 리스트 : 여러 개의 데이터를 순서대로 저장하는 자료형
# 리스트 생성
fruits = ["사과", "바나나", "포도"]
#print(fruits)

# 하나씩 꺼내기
print(fruits[0])    # 사과
print(fruits[1])    # 바나나
print(fruits[2])    # 포도

print()
print()

# 직접 추가하기
fruits.append("딸기")
#print(fruits)

# 반복문과 같이 사용하기
for fruit in fruits:
    print(fruit)

print("==== 예제 =====")
foods = []
foods.append("치킨")
foods.append("피자")
foods.append("초밥")

print("좋아하는 음식")
for food in foods:
    print(food)