import requests

api_key = "361e0a1a4b7342b989e5f735f7d1cbe0"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=361e0a1a4b7342b989e5f735f7d1cbe0"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])

