import requests
from bs4 import BeautifulSoup

def fetch_news_articles(company_name):
    search_url = f"https://news.google.com/search?q={company_name}&hl=en-US&gl=US&ceid=US:en"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        
        # Extract article titles, links, and summaries
        for article in soup.find_all('article'):
            title = article.find('h3').text if article.find('h3') else ''
            summary = article.find('span', class_='xBbh9').text if article.find('span', class_='xBbh9') else ''
            link = article.find('a')['href'] if article.find('a') else ''
            
            articles.append({
                'title': title,
                'summary': summary,
                'link': f"https://news.google.com{link}" if link else ''
            })
            
            if len(articles) >= 10:  # Limit to 10 articles
                break
        return articles
    else:
        return None
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
from gtts import gTTS
import os

def text_to_speech(text, language='hi'):
    tts = gTTS(text=text, lang=language, slow=False)
    audio_filename = "tts_output.mp3"
    tts.save(audio_filename)
    return audio_filename
