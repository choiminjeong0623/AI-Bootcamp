# w : 기존 내용 삭제 후 새로 저장한다.
# a : 기존 내용을 유지하고 뒤에 계속 추가한다.

memo = input("메모를 입력하세요 : ")

with open("memo.txt", "a", encoding="utf-8") as file:
    file.write(memo + "\n")
print("메모 저장 완료!")

with open("memo.txt", "r", encoding="utf-8") as file:
    memoRead = file.read()

print("==== 저장된 메모 ====")
print(memoRead)