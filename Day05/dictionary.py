# Dictionary : 이름표(key)와 값(value)을 한 쌍으로 저장하는 자료형
student = {
    "name" : "최민정",
    "age" : 31,
    "dream" : "AI Engineer"
}

print(student["name"])
print(student["age"])
print(student["dream"])

print()

# 직접 추가하기
student["MBTI"] = "INFJ"
print(student["MBTI"])

print()

# 전체 출력하기
for key, value in student.items():
    print(key, value)