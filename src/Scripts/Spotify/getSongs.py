# getSongs.py
import pandas as pd
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
print("CLIENT_ID:", os.getenv("CLIENT_ID"))
print("CLIENT_SECRET:", os.getenv("CLIENT_SECRET"))

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    print(result.status_code, result.content)  # <-- Add this
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_tracks_by_emotion(token, emotion, limit=10):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={emotion}&type=track&limit={limit}"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    #print(json_result)
    
    tracks = []
    for item in json_result.get("tracks", {}).get("items", []):
        track_name = item["name"]
        artist_name = item["artists"][0]["name"]
        tracks.append(f"{track_name} - {artist_name}")
    return tracks

df = pd.read_csv("../DataExtraction/emotions.csv")
dominant_emotion = df['Emotion'].value_counts().idxmax()  

print(f"Dominant Emotion: {dominant_emotion}")

token = get_token()
tracks = search_tracks_by_emotion(token, dominant_emotion)

print("\nTop Spotify tracks for emotion:")
for t in tracks:
    print(t)
