import requests
from send_email import send_email

api_key = "361e0a1a4b7342b989e5f735f7d1cbe0"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=361e0a1a4b7342b989e5f735f7d1cbe0"

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Send email fuction


body = ""

# Access the article titles and description
for article in content["articles"]:
    body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body.encode("utf-8")
send_email(body)

