from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
import pandas as pd

class DatabaseManager:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        self.connection = self.engine.connect()
        self.metadata = MetaData()
    
    def create_tables(self):
        tweets = Table(
            'tweets', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('text', String(255)),
            Column('sentiment_id', Integer, ForeignKey('sentiments.sentiment_id'))
        )
        
        sentiments = Table(
            'sentiments', self.metadata,
            Column('sentiment_id', Integer, primary_key=True),
            Column('sentiment_label', String(255))
        )
        
        self.metadata.create_all(bind=self.engine)
    
    def insert_from_csv(self, csv_file, table_name):
        df = pd.read_csv(csv_file)
        # df.to_sql('tweets', con=self.engine, if_exists='append', index=False)
        df.to_sql('tweets', con=self.engine, if_exists='append', index=False, index_label=None)
if __name__ == "__main__":
    db_manager = DatabaseManager('mysql://root@127.0.0.1:3306/sentiments')
    db_manager.create_tables()
    db_manager.insert_from_csv('sentiment_good.csv', 'tweets')
    db_manager.insert_from_csv('sentiment_bad.csv', 'tweets')
    db_manager.insert_from_csv('sentiment_neutral.csv', 'tweets')
    db_manager.insert_from_csv('sentiment_counts.csv', 'sentiments')
