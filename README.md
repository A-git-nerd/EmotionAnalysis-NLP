# Emotion Analysis + Spotify Track Hashtags

A Python project that analyzes text to detect emotions, cleans the data, and recommends Spotify tracks related to the dominant emotion, complete with **hashtags** generated from audio features and artist genres.

## Features

* **Clean Chat Data:** Remove noise, unnecessary characters, and prepare text for analysis.
* **Text Emotion Detection:** Uses `j-hartmann/emotion-english-distilroberta-base` for classifying emotions in text.
* **Dominant Emotion Extraction:** Finds the most frequent emotion in a dataset.
* **Spotify Track Search:** Fetches tracks related to the detected emotion.
* **Hashtag Generation:** Creates hashtags from artist genres and audio features like `#happy`, `#energetic`, `#danceable`.

## Requirements

* Python 3.13.7
* Spotify Developer Account
* `.env` file containing:

```env
TASK=text-classification
MODEL_NAME=j-hartmann/emotion-english-distilroberta-base

SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
```

* Python packages:

```bash
pip install -r requirements.txt
```

## Project Structure

```
SENTIMENTANALYSIS/
│
├─ .env
├─ requirements.txt
├─ .gitignore
│
├─ src/
│   ├─ Data/
│   │   ├─ chat.txt
│   │   └─ typesEmotion.txt
│   │
│   ├─ Scripts/
│       ├─ DataExtraction/
│       │   ├─ chat.ipynb          # Cleaning & preparing chat data
│       │   ├─ cleaned_chat.csv
│       │   └─ emotions.csv
│       │
│       ├─ EmotionAnalysis/
│       │   └─ analysis.py         # Fetch dominant emotion
│       │
│       ├─ Model/
│       │   └─ model.py
│       │
│       └─ Spotify/
│           ├─ __pycache__/
│           ├─ emotion_to_genre.py
│           ├─ getEmotion.py
│           └─ getSongs.py
```

## Workflow

### 1. Clean Chat Data

* Load raw chat data (`chat.txt`)
* Remove unnecessary characters, empty lines, or irrelevant text
* Save cleaned data as `cleaned_chat.csv`

### 2. Fetch Emotion

* Use the cleaned CSV to predict emotions for each line
* Save results in `emotions.csv`
* Extract the **dominant emotion** for the dataset

### 3. Get Spotify Tracks

* Use the dominant emotion to search Spotify tracks
* Fetch artist genres and audio features (`valence`, `energy`, `danceability`)
* Generate hashtags for each track
* Print track names with hashtags

## Example Usage

```bash
# Step 1: Clean Data
python src/Scripts/DataExtraction/chat.ipynb

# Step 2: Fetch Emotion
python src/Scripts/EmotionAnalysis/analysis.py

# Step 3: Get Songs
python src/Scripts/Spotify/getSongs.py
```

**Example Output:**

```
Dominant Emotion: neutral

Top Spotify tracks with hashtags:
Blinding Lights - The Weeknd
Hashtags: #pop #rnb #energetic #danceable
Happy - Pharrell Williams
Hashtags: #pop #funk #hiphop #happy #energetic #danceable
```
