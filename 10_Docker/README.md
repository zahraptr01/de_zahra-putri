Rangkuman Materi Docker
1.	Virtual Machine (VM) adalah sebuah representasi virtual dari sebuah computer dimana berbagai program dapat dijalankan di dalam VM
2.	Container adalah sebuah unit yang “membungkus” kode beserta dependensi (library) sehingga aplikasi dapat dijalankan dengan cepat dan andal (reliable) di berbagai environment
3.	Salah satu container yang popular adalah docker, tugas utama docker adalah mengelola berbagai container
4.	Docker adalah sebuah container manager yang dapat digunakan untuk mengelola aplikasi dalam bentuk container
5.	Docker run digunakan untuk membuat dan menjalankan container. Docker build digunakan untuk membuat sebuah docker images dari aplikasi yang telah dibuat. Docker pull digunakan untuk mengunduh docker image yang telah dibuat
6.	Docker volume adalah sebuah mekanisme penyimpanan data yang dapat digunakan agar data tetap ada (persistent)
7.	Dengan menggunakan docker volume proses backup data dan migrasi data lebih mudah, data dapat dibagi lebih aman dengan container lain, dan dapat menambahkan fungsionalitas lain
8.	Docker network adalah sebuah jaringan yang dapat digunakan antar container untuk berkomunikasi satu sama lain
9.	Container Orchestration adalah sebuah mekanisme untuk mengelola berbagai container. Container orchestraction cocok digunakan untuk mengelola sistem yang dibangun dnegna berbagai container seperti microservices
10.	Docker Compose adalah sebuah container orchestrain yang sudah disediakan oleh docker. Docker compose dapat digunakan untuk menjalankan berbagai container dengan membuat file konfigurasi dalam format YAML
