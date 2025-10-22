import pandas as pd
from Scripts.Model.model import get_emotion

df = pd.read_csv("../DataExtraction/cleaned_chat.csv")

df["Emotion"] = df["Message"].apply(get_emotion)

df.to_csv("../DataExtraction/emotions.csv",index=false)

print("Done!")
