import requests

url = "https://aladhan.p.rapidapi.com/timingsByCity"

headers = {
    'x-rapidapi-host': "aladhan.p.rapidapi.com",
    'x-rapidapi-key': "32c8012af0msh875fd99240cf346p17e9b0jsn80f61811c9a9",
    'city': "paris",
    'country': "france"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)