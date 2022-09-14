# TUGAS 2 PBP

Nama : Risa Lestari

NPM : 21066555274

Kelas: PBP - C

Link Deployment: https://tugas-2-pbp-2022.herokuapp.com/katalog/
<br/>

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

</br>
![gambarBagan] (/images/gambarBagan.png)
</br>

Django merupakan sebuah framework web development dengan menggunakan Bahasa python serta berpola Model Template Views (MVT). Ketika user melakukan request, maka url yang diberikan akan masuk ke URLConf. Jika url yang diberikan sudah sesuai, kemudian view (di views.py) akan memberikan suatu response kepada user berupa tampilan yang akan ditampilkan di template (yang berisi file.html). Hal ini dinamakan static website. Berbeda dengan dinamis website yang content dari websitenya berubah-ubah berdasarkan data dari database nya. Proses dinamis website, yaitu pertama, user akan melakukan suatu request dan akan dilakukan proses screening di URLConf untuk mengecek apakah request yang dikirim user ada atau tidak. Apabila user membutuhkan suatu data dari database, maka views akan mencari data yang dicari user di database melalui models (representasi dari sebuah database). Models berfungsi untuk menghubungkan views dengan database dan akan mengembalikan data yang di request oleh user. Lalu, views akan mengirimkan data tersebut ke templates (file.html)

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Ketika kita ingin mengerjakan suatu Python project, maka kita membutuhkan sebuah virtual environment. Virtual environment adalah tempat untuk menyimpan seluruh kebutuhan library yang kita butuhkan dalam project yang akan dikerjakan. Hal ini penting karena pada saat kita mengerjakan sebuah project python, pastinya kita membutuhkan library-library untuk mendukung project kita. Misalnya, kita ingin meng-install library numpy kemudian library tersebut di-install tanpa menggunakan virtual environment. Maka, numpy yang sudah terpasang akan menggunakan base environment yang ada di komputer atau laptop kita. Namun, apabila project kita ingin berpindah device, maka library tersebut tidak ikut terbawa. Pada akhirnya, pada device yang baru kita harus install lagi library-library yang kita butuhkan. Hal ini sangat merepotkan karena kita harus tahu versi-versi dari setiap library-nya tersebut. Maka dari itu, kita membutuhkan virtual environment.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Pada saat pembuatan aplikasi baru pada django project, pertama kita harus membuat url (terdapat pada folder django project atau root folder) yang akan dijadikan sebagai routing pada saat user ingin mengunjungi halamannya. Kemudian, membuat sebuah folder templates yang berisi file.html yang akan menampilkan tampilan halaman kepada user. Pada file urls.py yang ada di django app, import path yang berada di package django.urls dan import function yang terdapat di views (dalam project saya function bernama show_katalog). Function tersebut melakukan suatu pengambilan data dari models dengan perintah CatalogItem.objects.all() untuk mendapatkan data-data dari models yang berasal dari database. Kemudian, data-data tersebut di-render ke halaman html yang akan dituju dan halaman tersebut dapat menampilkan/memetakan data-data dalam bentuk response dari views kepada user. Pada tahap akhir, dilakukan deployment ke Heroku. Pertama, membuat sebuah repositori baru di GitHub yang akan digunakan sebagai repositori aplikasi Django. Kedua, lakukan git init pada direktori django yang telah dikerjakan sebelumnya dan atur origin dari repositori git lokal baru tersebut ke repositori GitHub yang telah dibuat. Ketiga, buatlah sebuah file bernama Procfile, dpl.yml, dan .gitignore. Lalu Add, commit, dan push perubahan yang telah dilakukan ke GitHub repo kita. Setelah melakukan prosedur tersebut, aplikasi Django siap untuk di-deploy ke Heroku. Tambahkan variabel repository secret baru untuk melakukan deployment. Seperti:
</br>
HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
</br>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
