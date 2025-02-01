import requests
from datetime import date

topic = "tesla"
url = (f"https://newsapi.org/v2/everything?q={topic}"
       "&sortBy=publishedAt"
       "&apiKey=dbe17092c3b942188364fc8149ea9170&language=en")

raw_request = requests.get(url)
content = raw_request.json()

message = ""
for article in content["articles"]:
    Title = article.get("title", "No Title Available")
    Description = article.get("description", "No Description Available")
    Url = article.get("url", "No URL Available")

    if article:
        message += f"Subject: Today's news\n{Title}\n{Description}\n{Url}\n\n"

print(message)