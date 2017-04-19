from flask import Flask,jsonify,request
import json
from storage_tweets import Storage


app = Flask(__name__)


@app.route("/tweets",methods=['GET'])
def get_tweets():
    return jsonify(Storage.get_all_tweets())


@app.route("/tweets/<int:tweet_id>",methods=['GET'])
def get_tweet(tweet_id):
    return jsonify(Storage.get_single_tweet(tweet_id))


@app.route("/tweets",methods=['Post'])
def post_tweet():
    if not request.get_data():
        return "No new data"
    else:
        received_data = json.loads(request.get_data())
        Storage.saving_new_tweet(received_data["tweet"])
        print(request.json)
        return "The tweet has been saved", 201


@app.route("/tweets/<int:tweet_id>",methods=['DELETE'])
def delete_tweet(tweet_id):
    return jsonify(Storage.delete_single_tweet(tweet_id)),204


if __name__ == "__main__":
    app.run()