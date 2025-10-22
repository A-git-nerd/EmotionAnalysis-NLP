# Model from Hugging face https://huggingface.co/j-hartmann/emotion-english-distilroberta-base?library=transformers
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
model = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")