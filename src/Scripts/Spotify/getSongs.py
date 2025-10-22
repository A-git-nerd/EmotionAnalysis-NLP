import pandas as pd
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

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
    result.raise_for_status()
    json_result = json.loads(result.content)
    return json_result["access_token"]

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_audio_features(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    return result.json()

def search_tracks_by_emotion(token, emotion, limit=10):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={emotion}&type=track&limit={limit}"
    result = get(url + query, headers=headers)
    json_result = result.json()
    
    tracks = []
    for item in json_result.get("tracks", {}).get("items", []):
        track_name = item["name"]
        artist_name = item["artists"][0]["name"]
        track_id = item["id"]
        artist_id = item["artists"][0]["id"]

        artist_info = get(f"https://api.spotify.com/v1/artists/{artist_id}", headers=headers).json()
        genres = artist_info.get("genres", [])
        #print(genres)

        features = get_audio_features(token, track_id)
        tags = genres.copy()

        if features.get("valence", 0) > 0.7:
            tags.append("happy")
        elif features.get("valence", 0) < 0.3:
            tags.append("sad")
        if features.get("energy", 0) > 0.8:
            tags.append("energetic")
        if features.get("danceability", 0) > 0.7:
            tags.append("danceable")
        
        hashtags = ["#" + tag.replace(" ", "") for tag in tags]

        tracks.append({
            "track": f"{track_name} - {artist_name}",
            "hashtags": hashtags
        })
    return tracks

df = pd.read_csv("../DataExtraction/emotions.csv")
dominant_emotion = df['Emotion'].value_counts().idxmax()  
print(f"Dominant Emotion: {dominant_emotion}")

token = get_token()
tracks = search_tracks_by_emotion(token, dominant_emotion)

print("\nTop Spotify tracks with hashtags:")
for t in tracks:
    print(t["track"])
    print("Hashtags:", " ".join(t["hashtags"]))
