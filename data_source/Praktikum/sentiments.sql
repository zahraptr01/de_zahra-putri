USE schema_sentiments;

CREATE TABLE sentiments (
    sentiment_id INT PRIMARY KEY AUTO_INCREMENT,
    sentiment_label VARCHAR(255)
);

CREATE TABLE tweetss (
    id INT PRIMARY KEY AUTO_INCREMENT,
    text TEXT,
    sentiment_id INT,
    FOREIGN KEY (sentiment_id) REFERENCES sentiments(sentiment_id)
);