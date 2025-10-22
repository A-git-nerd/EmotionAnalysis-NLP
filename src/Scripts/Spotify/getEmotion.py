import pandas as pd

df = pd.read_csv("../DataExtraction/emotions.csv")

dominant_emotion = df['Emotion'].value_counts().idxmax()
print(f"Emotion: {dominant_emotion}")