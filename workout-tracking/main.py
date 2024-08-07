import requests

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")
