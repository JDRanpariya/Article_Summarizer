from django.db import models
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# Load summarizer once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def get_summary(content, max_chunk=300):
    sentences = content.split(". ")
    chunks, current_chunk = [], []
    
    for sentence in sentences:
        words = sentence.split(" ")
        if len(current_chunk) + len(words) <= max_chunk:
            current_chunk.extend(words)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = words
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    res = summarizer(chunks, max_length=70, min_length=20, do_sample=False)
    return " ".join(r["summary_text"] for r in res)

def scrape_article(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    # Better: only <p> tags
    text = " ".join([p.get_text() for p in soup.find_all("p")])
    return text.strip()

class Article(models.Model):
    url = models.URLField(max_length=500, unique=True)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.content and self.url:
            self.content = scrape_article(self.url)
        if not self.summary and self.content:
            self.summary = get_summary(self.content)
        super().save(*args, **kwargs)
