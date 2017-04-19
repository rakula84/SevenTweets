import requests
import json

url = "http://127.0.0.1:5000/tweets"

#Get all tweets
req = requests.get(url)
print("You may view all tweets below -\n", req.text)
print("Status code:", req.status_code)

#Get tweet by id
req2 = requests.get("http://127.0.0.1:5000/tweets/2")
print("Results:\n", req2.text)
print("Status code:", req2.status_code)

#Posting new tweet
pos = requests.post(url, json={"tweet":"This is the second one"})
print("Status:\n", pos.text)
print("Status code:", pos.status_code)

#Posting one more tweet
pos2 = requests.post(url, json={"tweet":"This is tweet number 3"})
print("Status code:", pos2.status_code)
print("Status code:", pos2.status_code)

#Deleting tweet by id
dele = requests.delete("http://127.0.0.1:5000/tweets/4")
print("Status\n", dele.text)
print("Status code\n", dele.status_code)