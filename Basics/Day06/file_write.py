# 파일 쓰기
file = open("hello.txt", "w", encoding="utf-8")

file.write("안녕하세요.\n")
file.write("Day06 파일 저장 연습입니다.")

file.close()

print("파일 저장이 완료되었습니다.")