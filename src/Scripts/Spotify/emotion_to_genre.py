from src.Scripts.Spotify.getEmotion import dominant_emotion

emotion_to_genre = {
    "joy": "pop",
    "sadness": "acoustic",
    "anger": "metal",
    "disgust": "punk",
    "fear": "ambient",
    "surprise": "dance",
    "neutral": "chill"
}

target_genre = emotion_to_genre.get(dominant_emotion, "pop")