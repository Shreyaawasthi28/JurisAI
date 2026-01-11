from transformers import pipeline

# Lightweight T5 model for summarization
summarizer = pipeline("summarization", model="t5-small")

def generate_summary(text):
    summary = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )
    return summary[0]["summary_text"]
