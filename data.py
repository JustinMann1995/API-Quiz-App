import requests

parameters = {
    "amount" : 10,
    "type" : "boolean",
}

# grabs random trivia questions from API as a json
response = requests.get(url="https://opentdb.com/api.php", params= parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
