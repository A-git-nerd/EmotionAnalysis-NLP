import pandas as pd
from src.Scripts.Model.model import emotion_detect

df = pd.read_csv("../DataExtraction/cleaned_chat.csv")

df["Emotion"] = df["Message"].apply(emotion_detect)

df.to_csv("../DataExtraction/emotions.csv",index=False)

print("Done!")
