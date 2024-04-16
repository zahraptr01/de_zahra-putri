Rangkuman Materi Workflow Orchestraction with Airflow
1.	Workflow adalah sekumpulan tugas yang terhubung satu sama lain untuk mencapai tujuan tertentu yang dalam Apache Airflow akan digambarkan dalam sebuah graf (Directed Acyclic Graph / DAG). 
2.	Task adalah sebuah tugas yang digunakan untuk menjalankan aktivitas tertentu atau tugas yang diselesaikan dari sebuah workflow.  
3.	Operator adalah sebuah komponen yang digunakan untuk menjalankan sebuah task.
4.	DAG bersifat satu arah, bisa terdiri dari berbagai task dengan operator yang berbeda, setiap task atau node dapat memiliki cabang menuju task lainnya, dan berbagai task bisa menuju satu task yang sama.
5.	Apache Airflow adalah sebuah tools yang dapat digunakan untuk mengelola workflow.
6.	XCOM adalah sebutan dari cross communication yang memungkinkan antar task dapat bertukar atau mengirim data. XCOM cocok digunakan untuk data dengan ukuran kecil, tidak cocok untuk data dengan ukuran besar seperti sebuah DataFrame, file, dan data lain.
7.	Taskflow dapat digunakan untuk membuat sebuah data pipeline di Airflow.
8.	DAG dijalankan menggunakan library Python yang sudah built-in sehingga jika membutuhkan library eksternal tambahan maka perlu menyiapkan Docker Image yang dibuat secara custom. Custom Image dapat digunakan untuk menjalankan sebuah DAG yang membutuhkan depedensi/library tambahan yang belum tersedia secara default di Python.
9.	Pada Apache Airflow terdapat fitur untuk mengirim email jika DAG mengalami kegagalan atau berhasil dijalankan. Konfigurasi email bisa disesuaikan dengan SMTP yang digunakan bisa juga dengan menggunakan SMTP lokal seperti MailHog sebagai percobaan.
