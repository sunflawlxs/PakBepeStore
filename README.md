# MELAKUKAN INISIASI GITHUB

Pada langkah ini saya telah memastikan kalau sudah memiliki akun GitHub karena saya akan melakukan inisiasi repositori di GitHub yang telah saya miliki. 

1. Buka akun GitHub, kemudian buatlah Repositori Baru dengan nama "PakBepeStore", pastikan sudah mengatur visibilitas proyek sebagai "Public" dan biarkan pengaturan lainnya pada nilai default. 
2. Membuat direktori lokal di komputer yang telah diinisasi dengan Git. Kemudian menambahkan berkas README.md. Isi berkas tersebut dengan kata-kata atau kalimat yang bisa disesuaikan atau bisa menggunakan "tes" untuk sementara. 
3. Setelah itu bukalah terminal di folder yang telah kamu buat kemudian clone ke akun GitHub dengan repository yang kamu buat sebelumnya. 
```git clone <URL_CLONE>``` (gantilah URL_CLONE dengan URL yang telah kamu salin).
4. Kemudian di dalam folder kita membuat direktori baru dengan nama PakBepeStore dengan menjalankan perintah 
```
mkdir PakBepeStore
cd PakBepeStore
```
5. Setelah itu kita membuat virtual environment dengan menjalankan perintah 
```python -m venv env```
6. Setelah berhasil membuat virtual environment kita bisa mengaktifkannya dengan perintah. 
```env\Scripts\activate.bat```

# Menyiapkan Dependencies dan Membuat Proyek Django
1. Di dalam direktori yang sama, kita membuat ```requirements.txt``` dan menambahkan beberapa dependencies. 
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
2. Kita membuat aplikasi Django baru bernama PakBepeStore dengan perintah 
```django-admin startproject PakBepeStore .```
3. Setelah itu untuk keperluan deployment kita bisa menambahkan ```*``` pada ```ALLOWED_HOSTS``` di ```settings.py```
```* ALLOWED_HOSTS = ["*"]```
4. Kemudian pastikan berkas manage.py ada pada direktori yang aktif dengan menjalankan perintah 
```./manage.py runserver```
kita bisa mengecek http://localhost:8000 untuk melihat apakah aplikasi Django kamu berhasil dibuat atau tidak. 
5. Untuk menghentikan server, tekan ```Ctrl+C```. 

# UNGGAH PROYEK KE REPOSITORI GITHUB
1. Tambahkan berkas ```.gitignore``` di dalam folder PakBepeStore dengan teks berikut
   
```python
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

# Membuat Aplikasi main dalam Proyek Shopping List
1. Jalankan perintah ini unntuk membentuk direktori baru untuk membentuk direktori baru dengan nama main
```
python manage.py startapp main
```
2. mendaftarkan aplikasi main ke dalam proyek Buka berkas ```settings.py``` di dalam direktori proyek PakBepeStore

Temukan variabel ```INSTALLED_APPS```.

Tambahkan 'main' ke dalam daftar aplikasi 
```
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
3. kemudian sekarang kita membuat direktori baru bernama templates di dalam direktori aplikasi ```main```. di dalam direktori tersebut kita membuat berkas baru bernama ```main.html``` dengan isi 
```
<h1>PakBepeStore Page</h1>

<h5>App Name: </h5>
<p>PakBepeStore</p> 
<h5>Class: </h5>
<p>PBP D</p>
```

4. buka berkas ```models.py``` pada direktori aplikasi main.

5. Isi berkas ```models.py``` dengan kode berikut.
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
```
6. Jalankan perintah berikut untuk membuat migrasi model.
```
python manage.py makemigrations
```
7. Jalankan perintah berikut untuk menerapkan migrasi ke dalam basis data lokal.
```
python manage.py migrate
```
8. Kemudian bukalah berkas ```views.py``` yang terletak di dalam berkas aplikasi main. tambahkan baris impor dibagian paling atas 
```from django.shortcuts import render```

9. tambahkan fungsi ```show_main``` dibawah impor: 
```
def show_main(request):
    context = {
        'name': 'PakBepeStore',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
```
10. buka kembali ```main.html``` di direktori ```templates``` pada direktori ```main```

11. ubah nama dan kelas yang dibuat 
```
...
<h5> App Name: </h5>
<p>{{ PakBepeStore }}<p>
<h5>Class: </h5>
<p>{{ D }}<p>
...
```
12. setelah itu kita membuat berkas ```urls.py``` di dalam direktori main. isi dengan kode berikut 
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
13. Buka berkas ```urls.py``` di dalam direktori proyek PakBepeStore, bukan yang ada di dalam direktori aplikasi main. tambahkan 
```
...
from django.urls import path, include
...

urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
14. kemudian coba jalankan proyek django dengan perintah python manage.py runserver lalu buka ```http://localhost:8000/main/``` untuk melihat halaman yang dibuat

15. buka berkas tests.py pada aplikasi main. kemudian isi dengan kode berikut 
```
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
```
16. lalu jalankan tes dengan perintah 
```
python manage.py test
```
17. apabila sudah benar kita bisa add, commit, dan push
```
git add .
git commit -m "<pesan_commit>"
git push -u origin <branch_utama>
```
# Melakukan Deployment ke Adaptable
1. Sambungkan akun GitHub, kemudian tekan tombol New App dan pilih connect an Existing Repository
2. Pilih repository yang mau dihubungkan yaitu PakBepeStore dan pilih branch yang digunakan. 
3. Pilih ```Python App Template``` dan``` PostgreSQL ```sebagai tipe datanya.
4. Pilih versi python yang digunakan kemudian isi Start Command dengan ```python manage.py migrate && gunicorn PakBepeStore.wsgi```
5. Kemudian kalian bisa langsung melakukan deployment dan menunggunya hingga finish.

# Pengertian Virtual Environment
Virtual Environment adalah alat yang sangat berguna ketika kita membutuhkan dependencies yang berbeda-beda antara project satu dengan lainnya yang berjalan pada satu operasi yang sama. Virtual Environment sendiri digunakan untuk project yang berbasis python. Ada banyak alasan mengapa kita menggunakan virtual environment. Salah satunya adalah keamanan proyek, kita kita menggunakan virtual environment, proyek kita bisa terlindungi dari adanya potensi kerusakan atau konflik dengan sistem python yang ada di device. 

# Apakah kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
Bisa, tetapi disarankan untuk menggunakan virtual environment dalam pembuatan web berbasis Django untuk menghindari masalah potensial dan menjaga agar proyek kita tetap terorganisir, bersih dan mudah dikelola. 

# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img width="650" alt="Screen Shot 2023-09-12 at 19 50 08" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/b72a4075-98ae-433e-bfc0-2ccd741bfa4f">

Penjelasan langkah-langkah di atas:

User: Permintaan pertama datang dari user, seperti mengakses halaman beranda situs web yang ada.

URLs (urls.py): Permintaan tersebut pertama-tama diarahkan ke berkas urls.py. Berkas ini berisi daftar URL yang akan ditangani oleh Django. Setiap URL memiliki tautan ke tindakan (view) yang akan dijalankan saat URL tersebut diakses.

Views (views.py): Setelah URL ditentukan, tindakan (view) yang sesuai dengan URL tersebut dijalankan. Berkas views.py berisi logika yang mengatur bagaimana tampilan akan diberikan sebagai respons. Ini dapat melibatkan pengambilan data dari model, pengolahan data, dan kemudian menentukan berkas HTML mana yang akan digunakan.

Models (models.py): Dalam proses ini, jika diperlukan, data dapat diambil atau dimanipulasi melalui model yang didefinisikan dalam berkas models.py. Model ini mewakili struktur data dalam aplikasi, seperti tabel database atau objek Python.

Berkas HTML (Template): View kemudian memilih berkas HTML yang sesuai (template) untuk digunakan. Template ini berisi tampilan akhir yang akan dikirimkan ke klien. Biasanya, template ini memiliki variabel yang akan diisi dengan data dari model.

Response ke Klien: Setelah template diisi dengan data, tampilan akhir dikirim sebagai respons ke klien, yang kemudian ditampilkan di browser klien.

# Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
MVC (Model-View Controller)
Model View Controller atau yang dapat disingkat MVC adalah sebuah pola arsitektur dalam membuat sebuah aplikasi dengan cara memisahkan kode menjadi tiga bagian yang terdiri dari:

Model
Bagian yang bertugas untuk menyiapkan, mengatur, memanipulasi, dan mengorganisasikan data yang ada di database.

View
Bagian yang bertugas untuk menampilkan informasi dalam bentuk Graphical User Interface (GUI).

Controller
Bagian yang bertugas untuk menghubungkan serta mengatur model dan view agar dapat saling terhubung.

source: https://www.dicoding.com/blog/apa-itu-mvc-pahami-konsepnya/

MVT
The MVT (Model View Template) is a software design pattern. It is a collection of three important components Model View and Template. The Model helps to handle database. It is a data access layer which handles the data.
The Template is a presentation layer which handles User Interface part completely. The View is used to execute the business logic and interact with a model to carry data and renders a template.
Although Django follows MVC pattern but maintains it?s own conventions. So, control is handled by the framework itself.
There is no separate controller and complete application is based on Model View and Template. That?s why it is called MVT application.
Model: As an object that defines entities in the database and their configuration
View: The main logic of the application that will process incoming requests
Template: as the view that will be returned to the user

source: https://www.javatpoint.com/django-mvt

MVVM
MVVM (Model-View-ViewModel) adalah sebuah arsitektur atau pola desain software, yang memisahkan logika bisnis dengan logika presentasi atau kontrol antarmuka pengguna (UI) menjadi tiga lapisan, yaitu model, view, dan viewmodel. 
Model: tempat untuk logika bisnis dan data aplikasi, yang didapatkan dari viewmodel setelah menerima input pengguna melalui view. 

View: menentukan struktur, tata letak, teks, gambar, dan elemen antarmuka lainnya yang nantinya dilihat oleh pengguna. 

ViewModel: penghubung view dan model
source: https://revou.co/kosakata/mvvm#:~:text=MVVM%20adalah%20pola%20desain%20yang,Model%2C%20View%2C%20dan%20ViewModel.

# Perbedaan 
MVC: Model berfungsi sebagai penampung data dan logika bisnis, View hanya bertugas menampilkan data, dan Controller mengendalikan alur aplikasi.
Hubungan antara Model dan View diatur oleh Controller. View tidak tahu tentang Model, dan Model tidak tahu tentang View.
MVT: Mirip dengan MVC, Model dan View dipisahkan, tetapi dalam MVT, ada tambahan konsep "Template" yang mengontrol tampilan dan tata letak View.
Model berfungsi sebagai basis data dan logika bisnis, View bertanggung jawab untuk menampilkan data, dan Template mengatur tampilan.
MVVM: Mengenalkan konsep ViewModel, yang tidak ada dalam MVC dan MVT. ViewModel bertindak sebagai perantara antara Model dan View, mengelola tampilan, dan memungkinkan pemisahan yang lebih kuat antara logika bisnis dan tampilan.
ViewModel mengubah data dari Model ke format yang dapat ditampilkan oleh View, sehingga View menjadi lebih pasif dan lebih mudah diuji.

# Bonus
<img width="458" alt="Screen Shot 2023-09-12 at 21 55 38" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/9dff18fe-78fb-436c-a685-2758756aa8d2">
