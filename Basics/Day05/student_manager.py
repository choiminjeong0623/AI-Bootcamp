# 학생 성적 관리 프록램
# 학생 정보 저장
# student = {
#     "이름" : "최민정",
#     "국어" : 80,
#     "영어" : 90,
#     "수학" : 100
# }

name = input("학생 이름을 입력하세요 : ")
kor = int(input("국어 점수를 입력하세요 :"))
eng = int(input("영어 점수를 입력하세요 :"))
math = int(input("수학 점수를 입력하세요 :"))

student = {
    "이름" : name,
    "국어" : kor,
    "영어" : eng,
    "수학" : math
}

# 총점 계산
total = student["국어"] + student["영어"] + student["수학"]
print("총점 : ", total)
student["총점"] = total


# 평균
student["평균"] = total / 3
print("평균 : ", student["평균"])

print("==== 출력 ====")
for key, value in student.items():
    print(key, " : ", value)
