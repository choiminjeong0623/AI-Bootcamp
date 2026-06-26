# 학생 정보 저장 프로그램
import json

name = input("이름을 입력하세요 : ")
kor = int(input("국어 점수를 입력하세요 : "))
eng = int(input("영어 점수를 입력하세요 : "))
math = int(input("수학 점수를 입력하세요 : "))

student = {
    "이름" : name,
    "국어" : kor,
    "영어" : eng,
    "수학" : math
}

with open("student_data.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=4)

print("학생 정보가 저장되었습니다.")

print()
print("==== 학생 정보 ====")
with open("student_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print("이름 : ", data["이름"])
print("영어 점수 : ", data["영어"])
print("수학 점수 : ", data["수학"])
print("국어 점수 : ", data["국어"])