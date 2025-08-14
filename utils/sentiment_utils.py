from nltk.sentiment.vader import SentimentIntensityAnalyzer

def categorize_sentiment(score):
    if score >= 0.5:
        return "strongly_positive"
    elif score > 0.05:
        return "positive"
    elif score >= -0.05:
        return "neutral"
    elif score > -0.5:
        return "negative"
    else:
        return "strongly_negative"

def apply_sentiment(df, text_col="text"):
    sia = SentimentIntensityAnalyzer()
    df["sentiment_score"] = df[text_col].apply(lambda x: sia.polarity_scores(x)["compound"])
    df["sentiment"] = df["sentiment_score"].apply(categorize_sentiment)
    return df