import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
	"x-rapidapi-key": "12a8213947msh609a83d73988739p16628bjsn60dc541f0c37",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())