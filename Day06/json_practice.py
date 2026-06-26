# JSON : Python Dictionary를 파일에 저장하는 형식
import json

student = {
    "이름" : "최민정",
    "국어" : 90,
    "영어" : 100,
    "수학" : 95
}

with open("student_data.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=4)

print("JSON 파일 저장이 완료되었습니다.")

with open("student_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(data["이름"])
print(data["영어"])
print(data["수학"])
print(data["국어"])