import boto3

def sentiment(text):
    """This detects sentiment"""
    
    comprehend = boto3.client("comprehend")
    result = comprehend.detect_sentiment(
        Text=text,
        LanguageCode='en')
    return result['Sentiment']

