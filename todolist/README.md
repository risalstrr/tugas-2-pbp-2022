## Tugas 4 PBP

Nama : Risa Lestari

NPM : 2106655274

Kelas: PBP - C

Link Deployment: https://tugas-2-pbp-2022.herokuapp.com/todolist/login/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

Saat permintaan dibuat, aplikasi di bagian sisi server melakukan validasi permintaan tersebut yang diharapkan dan akan menolak permintaan jika CSRF token tidak ada atau tidak valid. CSRF Token dapat mencegah serangan CSRF yang akan membuat penyerang tidak mungkin melakukan permintaan HTTP yang secara sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Dikarena penyerang tidak dapat menentukan atau memprediksi nilai token CSRF pengguna, sehingga tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut. CSRF Token harus ada setiap terdapat form input data karena bersifat rahasia dan ditangani dengan cara yang aman sepanjang life cycle program. Biasanya tindakan yang efektif adalah mengirimkan token ke klien secara tersembunyi pada bagian Form HTML yang dikirimkan menggunakan metode POST. Token kemudian akan sisipkan sebagai parameter permintaan saat Form HTML.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Django Forms adalah seperangkat formulir HTML lanjutan yang dapat dibuat menggunakan python dan mendukung semua fitur formulir HTML dengan cara pythonic. Rendering Django Forms di dalam template terkadang terlihat berantakan tetapi dengan pengetahuan yang tepat tentang Django Forms dan atribut dari field, seseorang dapat dengan mudah membuat Form yang sangat baik dengan semua fitur canggih.Kita dapat membuat elemen <form> secara manual tanpa menggunakan generator. Cara membuatnya adalah membuat file forms.py dan import django forms class seperti

from django import forms

# creating a form

class InputForm(forms.Form):

    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())

Sekarang untuk merender formulir ini menjadi tampilan, pindah ke views.py dan buat home_view seperti di bawah ini.

from django.shortcuts import render
from .forms import InputForm

# Create your views here.

def home_view(request):
context ={}
context['form']= InputForm()
return render(request, "home.html", context)

Lalu, di template html nya

<form action = "" method = "post">
    {% csrf_token %}
    {{form }}
    <input type="submit" value=Submit">
</form>

Anda dapat mengecek hasil tampilan pada host dan port http://localhost:8000/

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user input data melalui form pada kolom input yang telah disediakan, lalu user klik tombol submit yang berarti user mengirimkan http request method bernama "POST". Pada tag form, biasanya di awal sudah dideklarasi jenis method apa yang akan direquest oleh user ketika mengklik tombol submit. Maka, pada saat user klik submit maka data-data yang diinput oleh user akan masuk ke dalam database melalui views.py yang akan menghubungkannya ke models kemudian ke database. Ketika user mengakses halaman yang berisi kumpulan data-data yang telah diinput dan disubmit (mengambil data dari database) maka data-data tersebut ditampilkan di file html dengan cara mendapatkan data tersebut melalui http request method "GET" dan models akan memberikan response data yang diminta oleh views berdasarkan request user melalui URL.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Buat sebuah django-app bernama todolist dengan perintah python manage.py startapp todolist.
2. Buka settings.py di folder project_django dan tambahkan aplikasi todolist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app yang sudah dibuat ke dalam proyek Django
3. Buka file models.py yang ada di folder todolist dan membuat model untuk database
4. Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
5. Jalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
6. Kemudian hubungkan models dengan views lalu ke template
7. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist.
8. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
9. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
10. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL
11. Lakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub dan auto deploy di heroku.
