import requests
from send_email import send_email

api_key = "54298616fb344eb59390d6aafdcc3b56"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-03-14&sortBy=publishedAt&apiKey=" \
      "54298616fb344eb59390d6aafdcc3b56"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
