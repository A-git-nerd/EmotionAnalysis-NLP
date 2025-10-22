# Model from Hugging face https://huggingface.co/j-hartmann/emotion-english-distilroberta-base?library=transformers
# Use a pipeline as a high-level helper
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

task = os.getenv("TASK")
model_name = os.getenv("MODEL_NAME")

pipe = pipeline(task, model=model_name)

def emotion_detect(text:str) -> str:
    if not text or not isinstance(text,str):
        return "neutral"
    try:
        # [{'label': 'joy', 'score': 0.9987}]
        result = pipe(text[:1024])[0] # limit to 1024 chars and taking first column only
        return result["label"]
    except Exception as e:
        print(f"Error: {e}")
        return "error" 