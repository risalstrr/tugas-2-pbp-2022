## Tugas 6 PBP

Nama : Risa Lestari

NPM : 2106655274

Kelas: PBP - C

Link Deployment: https://tugas-2-pbp-2022.herokuapp.com/todolist/login/

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous programming adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma Event-Driven Programming adalah salah satu teknik pemogramman yang konsep kerjanya tergantung dari kejadian atau event tertentu. Misalnya, ketika tombol A diklik maka nilai label 2 ditambah nilai label 3 dibagi nilai label 4. Jika tombol A diklik dan ternyata label satu berisikan penjumlahan. maka program yang dijalankan label 2 ditambah label 3.

Konsep Event-Driven Programming sama seperti konsep pemogramman menggunakan Procedure. Pemograman yang memiliki input, proses dan output. Namun, ada satu penambahan yang berbeda, yaitu konsep pemilihan untuk mengeksekusi proses programnya. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event/peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.

Salah satu penerapan dalam tugas ini adalah penggunaan method click pada AJAX POST yang berfungsi untuk memberikan suatu event kepada function (callback) dan kemudian function tersebut melakukan perintah di dalamnya.

## Jelaskan penerapan asynchronous programming pada AJAX.

Synchronous programming pada AJAX ini membuat kode yang kita tuliskan dijalankan secara berurutan. Hal ini sangat lemah ketika kita gunakan untuk melakukan sebuah pekerjaan yang berat, atau pekerjaan yang membutuhkan waktu yang belum dapat kita pastikan kapan pekerjaan itu selesai.

Jika kita melakukan pekerjaan tersebut secara synchronous, proses runtime akan terblokade hingga pekerjaan tersebut selesai dijalankan. Yang paling menakutkan adalah pengguna akan terganggu dengan adanya blocking tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1.  Buat view baru yang mengembalikan seluruh data task dalam bentuk JSON.
2.  Buat path /todolist/json yang mengarah ke view yang baru dibuat.
3.  Lakukan pengambilan task menggunakan AJAX GET.
4.  Buat sebuah tombol Tambah assignment baru yang membuka sebuah modal dengan form untuk menambahkan task.
5.  Buat view baru untuk menambahkan task baru ke dalam database.
6.  Buat path /todolist/add yang mengarah ke view yang baru dibuat.
7.  Hubungkan form yang telah dibuat di dalam modal ke path /todolist/add
8.  Tutup modal setelah penambahan task telah berhasil dilakukan.
9.  Melakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.
