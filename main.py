import requests

def main():
    api_key = "1662958beb314cf4b178ad67ccb4256a"
    url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={api_key}"

    req = requests.get(url).json()
    for article in req["articles"]:
        print(article["title"])
        print(article["description"])

if __name__ == "__main__":
    main()