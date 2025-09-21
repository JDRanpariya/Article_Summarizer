from django.db import models
from transformers import pipeline
from bs4 import BeautifulSoup as bs4
import requests
import time

summarizer = pipeline("summarization")

def getSummary(content):
        max_chunk = 300

        content = content.replace('.', '.<eos>') # here we replace .,? and ! with <eos> along with punctuation to get easy split of sentences without removing punctuation
        content = content.replace('?', '?<eos>')
        content = content.replace('!', '!<eos>')  
        content = content.replace('    ', '<eos>')      

        sentences = content.split('<eos>')

        current_chunk = 0 
        chunks = []
        for sentence in sentences:
            if len(chunks) == current_chunk + 1: 
                if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                    chunks[current_chunk].extend(sentence.split(' '))
                else:
                    current_chunk += 1
                    chunks.append(sentence.split(' '))
            else:
                print(current_chunk)
                chunks.append(sentence.split(' '))

        for chunk_id in range(len(chunks)):
            chunks[chunk_id] = ' '.join(chunks[chunk_id])

        res = summarizer(chunks, max_length=70, min_length=20, do_sample=False)

        full_summary = ''.join([summ['summary_text'] for summ in res])

        return full_summary

def scrapeArticle(url):

    raw_res = requests.get(url)
    soup = bs4(raw_res.content, 'html.parser')
    raw_text = soup.text.replace("\n","").replace("\t","")
    word_count = int(len(soup.text.replace("\n","").replace("\t",""))/5)

    return raw_text

# Create your models here.

class urlIn(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField( blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'urlin'


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField(default=None, null=True)
    url = models.CharField(default=None, max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    summaryofarticle = models.TextField()
    
    def scrapeSave(self, *args, **kwargs):
        if not self.id:
            self.content = scrapeArticle(self.url)
            time.sleep(0.5)
            self.summaryofarticle = getSummary(self.content)
        
        return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
            self.summaryofarticle = getSummary(self.content)

        return super().save(*args, **kwargs)