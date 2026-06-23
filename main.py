import requests
from send_email import send_email

def main():
    api_key = "1662958beb314cf4b178ad67ccb4256a"
    url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}"
    topic = []

    req = requests.get(url).json()
    for article in req["articles"]:
        topic.append({"title" : article["title"], "description" : article["description"]})
    
    send_email(topic)

if __name__ == "__main__":
    main()