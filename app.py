import streamlit as st
from utils import fetch_news_articles, analyze_sentiment, text_to_speech

def main():
    st.title("Company News Sentiment Analyzer")
    
    company_name = st.text_input("Enter the Company Name", "")
    
    if company_name:
        articles = fetch_news_articles(company_name)
        
        if articles:
            st.write(f"Found {len(articles)} articles for {company_name}")
            
            sentiment_results = []
            
            for article in articles:
                sentiment = analyze_sentiment(article['summary'])
                sentiment_results.append({
                    'Title': article['title'],
                    'Summary': article['summary'],
                    'Sentiment': sentiment,
                    'Link': article['link']
                })
            
            st.write("Sentiment Analysis Results:")
            for result in sentiment_results:
                st.write(f"**Title**: {result['Title']}")
                st.write(f"**Summary**: {result['Summary']}")
                st.write(f"**Sentiment**: {result['Sentiment']}")
                st.write(f"[Read Full Article]({result['Link']})")
            
            # Convert summary to TTS (Text-to-Speech)
            final_summary = " ".join([f"{result['Title']}: {result['Sentiment']}" for result in sentiment_results])
            audio_filename = text_to_speech(final_summary)
            st.audio(audio_filename)
        else:
            st.write("No articles found or an error occurred.")
    
if __name__ == "__main__":
    main()
