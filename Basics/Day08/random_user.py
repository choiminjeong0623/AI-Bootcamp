import requests
import json

url = "https://randomuser.me/api/"

response = requests.get(url)

# print(response.status_code)
# print(response.json())

data = response.json()

name = data["results"][0]["name"]["first"]
country = data["results"][0]["location"]["country"]
email = data["results"][0]["email"]

# print("이름 : ", name)
# print("국가 : ", country)
# print("이메일 : ", email)

# JOSN 형태로 저장하려면 Dictionary 를 사용한다.
userData = {
    "name" : name,
    "country" : country,
    "email" : email
}

with open("random_user.json", "w", encoding="utf-8") as file:
    json.dump(userData, file, ensure_ascii=False, indent=4)

print("JSON 파일 저장이 완료되었습니다.")
