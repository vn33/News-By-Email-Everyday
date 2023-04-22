import requests
from send_email import send_email
topic = "tesla"

# get the api key from NewsApiorg
api_key = "your api key"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-03-14&" \
      "sortBy=publishedAt&" \
      "apiKey=" \
      "your api key&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's New!" + "\n" + body + article["title"] + "\n"\
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
