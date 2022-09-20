Nama: Risa Lestari
NPM : 2106655274
Link Deploy: https://tugas-2-pbp-2022.herokuapp.com/mywatchlist/

## Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON (JavaScript Object Notation) adalah format teks yang tidak bergantung pada bahasa pemrograman apapun. Ini didasarkan pada bahasa pemrograman JavaScript, mudah dimengerti, dan dihasilkan.

XML (Extensible markup language) dirancang untuk membawa data, bukan untuk menampilkan data. Extensible Markup Language (XML) adalah bahasa markup yang mendefinisikan seperangkat aturan untuk menyandikan dokumen dalam format yang dapat dibaca manusia dan dapat dibaca mesin. Tujuan desain XML fokus pada kesederhanaan, umum, dan kegunaan di Internet. Ini adalah format data tekstual dengan dukungan kuat melalui Unicode untuk bahasa manusia yang berbeda. Meskipun desain XML berfokus pada dokumen, bahasa ini banyak digunakan untuk representasi struktur data arbitrer seperti yang digunakan dalam layanan web.

HTML adalah bahasa yang relatif sederhana, dan mudah dipelajari untuk pemula. Namun, itu memang memiliki beberapa batasan dalam hal apa yang dapat Anda lakukan dengannya.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Kita membutuhkan data delivery untuk memudahkan mengirim data ke komputer lain dalam bentuk json atau xml.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buat sebuah django-app bernama mywatchlist dengan perintah python manage.py startapp mywatchlist.
2. Buka settings.py di folder project_django dan tambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah kamu buat ke dalam proyek Django
3. Buka file models.py yang ada di folder mywatchlist dan tambahkan potongan kode sesuai perintah soal
4. Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
5. Jalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
6. Buatlah sebuah folder bernama fixtures di dalam folder aplikasi mywatchlist dan buatlah sebuah berkas bernama initial_mywatchlist_data.json
7. Jalankan perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal.
8. Kemudian hubungkan models dengan views lalu ke template
9. lakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub dan auto deploy di heroku.

## HTML

![html](https://github.com/risalstrr/tugas-2-pbp-2022/blob/main/images/htmlPostman.png)

## XML

![xml](https://github.com/risalstrr/tugas-2-pbp-2022/blob/main/images/xmlPostman.png)

## JSON

![json](https://github.com/risalstrr/tugas-2-pbp-2022/blob/main/images/jsonPostman.png)
