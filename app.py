from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    params = {'q': '#lakers OR #warriors', 'result_type': 'recent', 'count': '100'}
    headers = {"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANAAPwEAAAAAMUf1p8IDnpwqOcGWjkXXI%2FxxEZE%3DJ9HbcXJ63q4w25cQWcwifyLV2GkmN0MiO10ARDV4sTD28bkcIo"}
    r = requests.get("https://api.twitter.com/1.1/search/tweets.json", params=params, headers=headers)
    to_json = r.json()
    tweets = to_json['statuses']
    parsed = [tweet['text'] for tweet in tweets]
    print(len(parsed))
    return str(parsed)
