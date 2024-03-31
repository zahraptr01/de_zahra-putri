Rangkuman Materi Data Warehouse dan Data Lake
1.	Data warehouse adalah sebuah sistem yang mengumpulkan data dari berbagai sumber yang nantinya dikumpulkan dalam satu tempat untuk keperluan analisis data, data mining, AI, dan machine learning
2.	Data warehouse memiliki data dari berbagai sumber (OS, ERP, CRM, SQK, dan Flat Files, Spreadsheets)
3.	Data yang telah dikumpulkan akan diproses melalui pipeline ETL (Extract, Transform, Load) yang terdiri darai tahap data validation, data cleaning, data transforming, data aggregating, dan data loading
4.	Setelah data diproses dan di load maka data akan dimasukkan ke data warehouse 
5.	Pada data lake tidak ada proses ETL baik dari berbagai sumber data. Data lake menyimpan data tidak terstruktur sedangkan data warehouse lebih terstruktur karena diolah terlebih dahulu
6.	Data lakehouse adalah sebuah arsitektur yang menggabungkan flesibilitas dan cost-efficiency dari data lake dengan manajemen data dan fitur struktur dari data warehouse
7.	Teknologi yang dapat dimanfaatkan untuk data warehouse yaitu AWS Redshift, Google Big Query, Clickhouse, Snowflake, Databricks, Apache Dorris, Postgre (Citus extension)
8.	Citus adalah sebuah extension yang bersifat open sources yang bisa digunakan pada postgresql sehingga data menjadi terdistribusi
9.	Dengan menggunakan citus, kita dapat melakukan sharded, replicated, parallelizes, compresses data, dan distribusi kueri
10.	Columnar table adalah sebuah mekanisme dimana kita dapat menyimpan data yang berorientasi pada kolom
