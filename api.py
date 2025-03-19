from flask import Flask, request, jsonify
from utils import fetch_news_articles, analyze_sentiment, text_to_speech

app = Flask(__name__)

@app.route('/news', methods=['GET'])
def get_news():
    company_name = request.args.get('company')
    articles = fetch_news_articles(company_name)
    return jsonify(articles)

@app.route('/sentiment-analysis', methods=['POST'])
def sentiment_analysis():
    data = request.json
    articles = data.get('articles', [])
    sentiment_results = []
    
    for article in articles:
        sentiment = analyze_sentiment(article['summary'])
        sentiment_results.append({
            'title': article['title'],
            'summary': article['summary'],
            'sentiment': sentiment
        })
    
    return jsonify(sentiment_results)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.json
    text = data.get('text', '')
    audio_filename = text_to_speech(text)
    return jsonify({'audio_file': audio_filename})

if __name__ == '__main__':
    app.run(debug=True)
