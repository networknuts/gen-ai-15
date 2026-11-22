import requests

owm_api_key = ""
owm_country_code = input("Enter your country code: ")
owm_zip_code = input("Enter your zip code: ")

owm_url = f"https://api.openweathermap.org/data/2.5/weather?zip={owm_zip_code},{owm_country_code}&appid={owm_api_key}"

response = requests.get(owm_url)

result = response.json()

print(result)