import pandas as pd
import numpy as np
import os

# 2. Data Ingestion dan Persiapan Data Lake / Data Werehouse
class DataLakeBuilder:
    def read_csv_data(self, file_path):
        return pd.read_csv(file_path)

    def handle_missing_values(self, df):
        return df.ffill().bfill()

    def handle_outliers(self, df, column):
        Q1, Q3 = df[column].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = np.clip(df[column], lower_bound, upper_bound)
        return df

    def save_to_parquet(self, df, file_name):
        df.to_parquet(file_name)

    def validate_data(self, file_path):
        df = pd.read_parquet(file_path)
        print(f"Ringkasan data pada file {file_path}:")
        print(df.head())
        print(df.describe())

dlb = DataLakeBuilder()
file_path = 'Code Competence 2/Praktikum/data_source/'

# Customer Feedback
feedback_df = dlb.read_csv_data(f'{file_path}customer_feedback.csv')
feedback_df = dlb.handle_missing_values(feedback_df)
feedback_df = dlb.handle_outliers(feedback_df, 'rating')
dlb.save_to_parquet(feedback_df, f'{file_path}customer_feedback.parquet')
dlb.validate_data(f'{file_path}customer_feedback.parquet')

# Customers
customers_df = dlb.read_csv_data(f'{file_path}customers.csv')
customers_df = dlb.handle_missing_values(customers_df)
customers_df = dlb.handle_outliers(customers_df, 'customer_id')
dlb.save_to_parquet(customers_df, f'{file_path}customers.parquet')
dlb.validate_data(f'{file_path}customers.parquet')

# Events
events_df = dlb.read_csv_data(f'{file_path}events.csv')
events_df = dlb.handle_missing_values(events_df)
events_df['date'] = pd.to_datetime(events_df['date'])
dlb.save_to_parquet(events_df, f'{file_path}events.parquet')
dlb.validate_data(f'{file_path}events.parquet')
dlb.validate_data('events.parquet')

# Tickets
tickets_df = dlb.read_csv_data(f'{file_path}tickets.csv')
tickets_df = dlb.handle_missing_values(tickets_df)
tickets_df = dlb.handle_outliers(tickets_df, 'event_id')
dlb.save_to_parquet(tickets_df, f'{file_path}tickets.parquet')
dlb.validate_data(f'{file_path}tickets.parquet')

# Transactions
transactions_df = dlb.read_csv_data(f'{file_path}transactions.csv')
transactions_df = dlb.handle_missing_values(transactions_df)
transactions_df = dlb.handle_outliers(transactions_df, 'ticket_id')
dlb.save_to_parquet(transactions_df, f'{file_path}transactions.parquet')
dlb.validate_data(f'{file_path}transactions.parquet')