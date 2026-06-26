# 파일 읽기
file = open("hello.txt", "r", encoding="utf-8")

content = file.read()
print(content)

file.close()