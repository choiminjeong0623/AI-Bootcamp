import requests
import json

# Open-Meteo API 사용
url = "https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

response = requests.get(url)
data = response.json()

current = data["current"]

print("현재 기온 : ", current["temperature_2m"], "°C")
print("습도 : ", current["relative_humidity_2m"], "%")
print("풍속 :", current["wind_speed_10m"], "km/h")