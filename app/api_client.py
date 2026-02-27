import requests

url = "https://en.wikipedia.org/w/api.php"

def get_random_pages(limit = 10):
  params = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnnamespace": 0,
    "rnlimit": limit
  }
  response = requests.get(url, params=params)
  response.raise_for_status()

  data = response.json()
  return data["query"]["random"]