import pandas as pd

class SentimentClassifier:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = None
        
    def load_data(self):
        self.data = pd.read_csv(self.dataset_path)
        
    def classify_sentiment(self):
        def categorize_sentiment(text):
            if 'good' in text.lower():
                return 'good'
            elif 'bad' in text.lower():
                return 'bad'
            else:
                return 'neutral'
        self.data['sentiment'] = self.data['tweets'].apply(categorize_sentiment)
        
    def save_to_csv(self):
        good_tweets = self.data[self.data['sentiment'] == 'good']
        bad_tweets = self.data[self.data['sentiment'] == 'bad']
        neutral_tweets = self.data[self.data['sentiment'] == 'neutral']
        
        good_tweets.to_csv("sentiment_good.csv", index=False)
        bad_tweets.to_csv("sentiment_bad.csv", index=False)
        neutral_tweets.to_csv("sentiment_neutral.csv", index=False)
        
    def summarize_counts(self):
        counts = self.data['sentiment'].value_counts()
        counts.to_csv("sentiment_counts.csv")
        
if __name__ == "__main__":
    classifier = SentimentClassifier("file.csv")
    classifier.load_data()
    classifier.classify_sentiment()
    classifier.save_to_csv()
    classifier.summarize_counts()