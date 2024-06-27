import pandas as pd
from google.cloud import storage

class DataWarehouseLoader:
    def __init__(self, data_lake_path, warehouse_bucket):
        self.data_lake_path = data_lake_path
        self.warehouse_bucket = warehouse_bucket

    def load_data(self):
        self.events_df = pd.read_parquet(f"{self.data_lake_path}events.parquet")
        self.customers_df = pd.read_parquet(f"{self.data_lake_path}customers.parquet")
        self.tickets_df = pd.read_parquet(f"{self.data_lake_path}tickets.parquet")
        self.transactions_df = pd.read_parquet(f"{self.data_lake_path}transactions.parquet")
        self.feedback_df = pd.read_parquet(f"{self.data_lake_path}customer_feedback.parquet")

    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        # Menggabungkan Data untuk Analisis
        # Gabungkan tabel transactions dengan tickets berdasarkan ticket_id
        merged_data = pd.merge(df_transactions, df_tickets, on='ticket_id')
        # Gabungkan dengan events berdasarkan event_id
        merged_data = pd.merge(merged_data, df_events, on='event_id')

        # Menghitung Jumlah Tiket yang Terjual per Acara
        tickets_sold_per_event = merged_data.groupby('event_id')['quantity'].sum().reset_index()

        # Menghitung Total Pendapatan dari Setiap Acara
        revenue_per_event = merged_data.groupby('event_id')['total_amount'].sum().reset_index()

        # Analisis feedback pelanggan
        # Gabungkan tabel customer_feedback dengan transactions berdasarkan transaction_id
        feedback_analysis = pd.merge(df_customer_feedback, df_transactions, on='transaction_id')
        # Hitung rating rata-rata per acara
        avg_rating_per_event = feedback_analysis.groupby('feedback_id')['rating'].mean().reset_index()

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event

    def save_to_warehouse(self, data_date):
        # Menyimpan data ke Google Cloud Storage
        # Inisialisasi klien Storage
        client = storage.Client()
        bucket = client.get_bucket(self.warehouse_bucket)

        # Menyimpan data yang telah ditransformasi
        self.tickets_sold_per_event.to_parquet(
            f"gs://{self.warehouse_bucket}/tickets_sold_per_event/{data_date}.parquet"
        )
        self.revenue_per_event.to_parquet(
            f"gs://{self.warehouse_bucket}/revenue_per_event/{data_date}.parquet"
        )
        self.feedback_analysis.to_parquet(
            f"gs://{self.warehouse_bucket}/feedback_analysis/{data_date}.parquet"
        )

data_lake_path = 'Code Competence 2/Praktikum/data_source/'
warehouse_bucket = 'cc2_alterra'
data_date = '2023-11-20'

dwl = DataWarehouseLoader(data_lake_path, warehouse_bucket)
dwl.load_data()
dwl.transform_data(dwl.transactions_df, dwl.tickets_df, dwl.events_df, dwl.feedback_df)
dwl.save_to_warehouse(data_date)