# Tautan Adaptable 
https://pakbepestore.adaptable.app/main/

# TUGAS PBP
<details>
<summary> TUGAS 2</summary>

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
</details>


<details>
<summary> TUGAS 3</summary>

 1. Membuat input form untuk menambahkan objek model pada app sebelumnya.
  * Pertama-tama saya membuka terminal di folder ```PakBepeStore``` dan mengaktifkan ```virtual environment``` seperti berikut 
```
source env/bin/activate
```

   * Kemudian saya membuka urls.py di folder ```PakBepeStore``` dan mengubah path main/ menjadi ```''``` pada ```urlpatterns``` seperti berikut
```
urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
```
   
   * Lalu mengimpplementasi Skeleton dengan membuat folder ```templates``` pada root folder dan buat base.html. isilah berkas base.html sebagai berikut:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
   * Lalu buka ```settings.py``` yang ada pada subdirektori PakBepeStore dan carilah baris yang mengandung ```TEMPLATES```. Kemudian sesuaikan kode berikut dengan yang sebelumnya sudah dibuat.
```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```
   * Pada subdirektori templates yang ada di ```main```, ubah kode ```main.html``` menjadi sebagai berikut 
```
{% extends 'base.html' %}

{% block content %}
    <h1>PakBepeStore Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```
   * Kemudian buat forms.py pada direktori ```main``` dengan kode 
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
   * Tambahkan import pada bagian atas di berkas ```views.py``` di folder ```main```
```
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```
   * Buat fungsi baru ```create_product``` seperti berikut
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
   * Ubah fungsi ```show_main``` yang sudah ada di ```views.py```
```
def show_main(request):
    products = Product.objects.all()

    context = {
        'AppName': 'PakBepeStore" ,
        'name': 'Sheryl', # Nama kamu
        'class': 'PBP D', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
```

   * import fungsi ```create_product``` di folder main di ```urls.py``` dan tambahkan path url di ```urlpatterns```
```
from main.views import show_main, create_product
```
```
path('create-product', create_product, name='create_product'),
```
   * Kemudian membuat berkas ```create_product.html``` pada direktori ```main/templates``` isi kode berikut: 
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
   * buka ```main.html``` tambahkan kode berikut 
```
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

 2. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
   * menambahkan beberapa fungsi dan import views.py di direktori main
```
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product

def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Sheryl Ivana',
        'class': 'PBP D', 
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

 3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
   * memodifikasi urls.py pada folder main dengan melakukan import dan menambahkan path 
```
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
```
# Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
 1. Apa perbedaan antara form POST dan form GET dalam Django?
-  Pengiriman data
  POST: data dikirim secara tersembunyi dan dikirim sebagai bagian dari body permintaan HTTP.
  GET: data dikirim melalui URL sebagai paramater quetry string. data inii dapat dilihat di dalam URL, yang membuat kurang aman untuk data yang sensitif.
-    Keamanan
  POST: lebih aman daripada GET karena data tidak terlihat di URL sehingga cocok untuk data yang sensitif.
   GET: kurang aman karena data terlihat dalam URL.
-   Penggunaan
  POST : Digunakan ketika Anda ingin mengirim data yang mengubah status server seperti menambah data baru
   GET: Digunakan  ketika Anda ingin mengirim data yang digunakan untuk permintaan pencarian atau ingin berbagi data lebih mudah dengan tautan
-    Cacheability
  POST: Tidak bisa dicache karena data dikirimkan sebagai bagian dari body permintaan HTTP
   GET: bisa dicache sehingga menghasilkan kinerja yang lebih baik di beberapa kasus.
-    Kemudahan Penggunaan
  POST: perlu lebih banyak pekerjaan untuk code nya untuk mengakses data karena data ga langsung di URL
   GET: data dikirim ke URL dan dapat diakses mudah melalui objek 'request.GET'
  
 # Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML (Extensible Markup Language)
  Tujuan utama: menyusun dan mentransfer data terstruktur antara sistem yang berbeda
  Struktur: menggunakan tag untuk menandai elemen data dan setiap elemen dapat memiliki atribut dan anak elemen.
-JSON (JavaScript Object Notation)
   Tujuan Utama: digunakan untuk pertukaran data ringan antara browser dan server serta antar aplikas web. digunakan juga dalam pengemabangan web dan API RESTful. 
   Struktur: mengandalkan sintaksis objek dalam JavaScript, yang terdiri dari pasangan nama-nilai sehingga membuat lebih mudah dibaca oleh mesin dan manusia.
- HTML (Hypertext Markup Language):
  Tujuan Utama: digunakan untuk membuat struktur dan tampilan halaman web. digunakan juga untuk merender halaman web dalam peramban web. 
   Struktur: menggunakan tag untuk menandai elem yang membentuk halaman web seperti teks, gambar, tautan, dan lainnya.

# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
1. Sintaksis lebih mudah dipahami
Menggunakan sintaksis yang mirip dengan objek dalam JavaScript yang membuatnya mudah dibaca dan diural oleh manusia. 
2. Ringan
Format data yang ringan yang berarti bahwa data yang dikirim dalam format JSON cenderung memiliki ukuran yang lebih kecil dibandingkan formmat lain. 
3. Dukungan luas
Hampir semua bahasa pemrograman memiliki dukungan JSON. ini membuat format datanya interoperabel yang berarti Anda mudah mengirim dan memnerima data JSON. 
4. Mendukung tipe data
JSON mendukung berbagai jenis data, termasuk string, angka, boolean, bojek, dan larik. Hal ini membantu agar lebih fleksibilitas dalam merepresntasikan data. 
5. Kode JavaScript yang bersih
JSON dapat digunakan dalam kode Java Script tanpa perlu proses parsing yang rumit. Ini memungkinkan aplikasi yang lebih bersih dan efisien, terutama ketika menghubungkan antara klien dan server.

# Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
```Link 1```
<img width="1259" alt="Screen Shot 2023-09-19 at 20 17 44" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/44e8c134-705f-41b4-aecf-7abc0d649a4c">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 17 48" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/b2c5bf9f-6209-4282-bbdc-fbcf52c18d33">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 17 55" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/70b02872-64c8-4cf9-9596-73cb178c58d2">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 01" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/e8e74749-d4de-4d39-8366-c18efa0e8d75">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 07" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/cdf92d4f-7d5a-47f4-9f3a-408ada5939ff">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 15" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/0a0bb9c0-8920-4f02-b56d-af00bd70f9ea">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 19" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/81845ba9-e4b3-4014-b70e-084a01e2a1cc">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 24" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/cf542352-424a-473a-b8f1-dc47a74fe43b">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 31" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/4934d656-39a4-472d-afbc-558c40d65451">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 18 34" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/48871e81-c57d-4601-acb2-280b3d0d0843">

```Link 2```
<img width="1259" alt="Screen Shot 2023-09-19 at 20 11 27" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/ef22912b-4147-4bf0-814d-4b1bcbc3fdcd">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 11 36" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/3144c1ce-8d8b-458d-874f-b59d3b472b07">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 11 42" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/7bbf8122-be94-4412-b570-2af5c8039dd2">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 11 51" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/229288ba-33b7-4761-829f-ff5a78d31298">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 11 59" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/2a2397d2-c92d-4512-97bb-1d828c6f0a6d">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 12 06" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/bfa966e9-3251-4d69-8e27-f98e68c14a9f">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 12 23" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/7894c0eb-b678-4830-8c47-22eb8d745a57">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 12 31" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/4ac5116d-d007-40b7-be2d-16ddca01068d">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 12 39" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/f2826fc0-62bf-4b0b-92b0-334a076a08e5">
<img width="1259" alt="Screen Shot 2023-09-19 at 20 12 45" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/d51eee21-ba7d-4bf5-9b6c-ad34cd2bb88d">

```Link 3```
<img width="1104" alt="Screen Shot 2023-09-19 at 19 57 19" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/2bbfa972-2e59-4a66-bdc7-7af1961e67a4">

```Link 4```
<img width="1104" alt="Screen Shot 2023-09-19 at 19 57 48" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/29b0b02e-380c-4722-8e4a-56a8fdb1da0c">

```Link 5```
<img width="1104" alt="Screen Shot 2023-09-19 at 19 56 13" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/4fbd0b99-2bc0-4b20-9646-4599615d34f2">
<img width="1104" alt="Screen Shot 2023-09-19 at 19 56 21" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/c37b2e42-7524-4b16-a1be-7cb24786f929">
<img width="1104" alt="Screen Shot 2023-09-19 at 19 56 28" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/b1951775-c161-4317-8000-6713eb9afd7c">
<img width="1104" alt="Screen Shot 2023-09-19 at 19 56 33" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/44347695-d1db-45ee-b019-7df05c4c4576">


BONUS 
Menambahkan pesan "Kamu menyimpan 2 item pada toko ini" (dengan X adalah jumlah data item yang tersimpan pada aplikasi) dan menampilkannya di atas tabel data. Kalimat pesan boleh dikustomisasi sesuai dengan tema aplikasi, namun harus memiliki makna yang sama. 
<img width="1259" alt="Screen Shot 2023-09-19 at 20 25 25" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/a281c419-8f27-4f81-8ae9-b785f913e65d">

 Melakukan add-commit-push ke GitHub.
```
git add .
git commit -m "done tugas 3"
git push -u origin main
```
</details>

<details>
<summary> TUGAS 4</summary>
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

- Menyalakan virtual environment di terminal. 

- Kemudian kita membuka views.py pada subdirektori main dan buat fungsi ```register``` yang menerima parameter ```request``` dan tambahkan import.

```
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```

```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- Kemudian membuat berkas html dengan nama register.html di folder main/templates. 
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
- kemudian buka urls.py dan import
```
from main.views import register 
```
dan tambahkan path url nya
```
...
path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
...
```
- kemudian untuk membuat fungsi login dan log out kita bisa menambahkan kode serta mengimport di main/views.py
```
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
```
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
    
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
- di urls.py kemudian kita menambahkan impor dan kode path url di ```urlpatterns```
```
from main.views import login_user
from main.views import logout_user
```
```
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
...
```
- kemudian kita buat berkas HTML baru dengan nama ```login.html``` di main/templates. 
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
- untuk logout, kita buka bekas ```main.html``` di folder main/templates. 
```
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```
2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
<img width="628" alt="Screen Shot 2023-09-26 at 20 04 08" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/9d407390-f26d-4d14-a53b-0065402a9ae8">
<img width="628" alt="Screen Shot 2023-09-26 at 20 03 54" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/4be0960b-b196-4719-9b2e-32072e7d71cc">


3. Menghubungkan model Item dengan User.
- buka ```models.py``` dan tambahkan kode
```
...
from django.contrib.auth.models import User
```
- tambahkan model product dengan kode berikut: 
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
- buka views.py dan ubah kode fungsi create_product:
```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
- ubah fungsi show_main
```
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```
- simpan perubahan dan lakukan migrasi dengan 
``` python manage.py makemigrations``` kemudian ketik 1 untuk menetapkan default value untuk field user. ketik angka 1 lagi untuk menetapkan user dengan ID 1. dan lakukan ```python manage.py migrate```. lalu jalankan proyek django dengan perintah ```python manage.py runserver``` dan buka http://localhost:8000/ 

4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- Menambahkan import pada main/views.py di bagian paling atas
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- memodifikasi fungsi login_user pada main/views.py dengan mengganti kode pada blok ```if user is not None```
```
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
- memodifikasi fungsi show_main dengan menambahkan ```'last_login':request.COOKIES['last_login']``` ke dalam variabel ```context```
```
context = {
    'name': 'Sheryl',
    'class': 'PBP D',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```
- kemudian ubah fungsi ```logout_user``` menjadi kode ini

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- dan tambahkan main.html

```
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```


 # Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
 Django UserCreationForm adalah salah satu komponen bawaan dalam framework web Python yang populer, Django. Form ini digunakan untuk membuat formulir pendaftaran atau pembuatan akun pengguna (user registration) dalam aplikasi web yang menggunakan Django. UserCreationForm secara khusus dirancang untuk menyederhanakan proses pembuatan akun pengguna dengan memungkinkan pengguna untuk mengisi informasi seperti username, password, dan email, serta data tambahan lainnya sesuai kebutuhan aplikasi.

Kelebihan dari Django UserCreationForm:

Integrasi yang Mudah: UserCreationForm telah terintegrasi dengan baik dengan Django, sehingga Anda dapat dengan mudah menggunakannya dalam proyek Django Anda tanpa perlu menulis kode tambahan yang rumit.

Validasi Otomatis: Form ini menyertakan validasi otomatis untuk memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan aturan yang ditentukan, seperti persyaratan password yang kuat.

Customizable: Anda dapat menyesuaikan UserCreationForm sesuai dengan kebutuhan aplikasi Anda dengan menambahkan atau mengubah bidang-bidang yang ada, serta menentukan pesan kesalahan yang sesuai.

Keamanan: UserCreationForm memastikan bahwa password yang dimasukkan oleh pengguna akan di-hash sebelum disimpan di database, menjaga keamanan informasi pengguna.

Kekurangan dari Django UserCreationForm:

Tidak Cocok untuk Kasus Khusus: Jika Anda memiliki kebutuhan yang sangat spesifik atau kompleks dalam hal pendaftaran pengguna, mungkin perlu menulis formulir pendaftaran kustom Anda sendiri daripada menggunakan UserCreationForm.

Tampilan Bawaan Mungkin Tidak Sesuai: Tampilan default dari UserCreationForm mungkin tidak sesuai dengan desain antarmuka Anda, sehingga Anda perlu menyesuaikannya untuk mencocokkannya dengan tampilan aplikasi Anda.

Pembatasan Fungsionalitas: Terkadang, UserCreationForm mungkin terlalu terbatas dalam hal fungsionalitas, terutama jika Anda perlu mengimplementasikan fitur-fitur tambahan seperti konfirmasi email, pilihan untuk peran pengguna, atau penambahan bidang-bidang kustom.

Dalam banyak kasus, UserCreationForm adalah alat yang sangat berguna untuk mempercepat pengembangan aplikasi web Django yang melibatkan otentikasi pengguna. Namun, tergantung pada kebutuhan proyek Anda, Anda mungkin perlu menyesuaikan atau menggantinya dengan formulir pendaftaran kustom agar sesuai dengan persyaratan aplikasi Anda.



 # Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
 Autentikasi (Authentication):

Definisi: Autentikasi adalah proses untuk memeriksa dan mengidentifikasi pengguna yang mencoba mengakses sistem atau aplikasi web. Ini berarti memverifikasi apakah pengguna adalah pengguna yang dia klaim.
Fungsi: Autentikasi memungkinkan sistem untuk mengetahui siapa yang sedang menggunakan aplikasi. Ini biasanya melibatkan pemeriksaan identitas pengguna berdasarkan informasi login, seperti username dan password.
Dalam Django: Django menyediakan berbagai mekanisme autentikasi bawaan, termasuk otentikasi berbasis sesi, otentikasi berbasis token, dan integrasi dengan berbagai metode otentikasi eksternal (misalnya, otentikasi OAuth dengan media sosial).
Otorisasi (Authorization):

Definisi: Otorisasi adalah proses untuk mengontrol akses pengguna terhadap sumber daya atau tindakan tertentu dalam aplikasi. Ini menentukan apa yang dapat dan tidak dapat dilakukan oleh pengguna setelah mereka berhasil diautentikasi.
Fungsi: Otorisasi mengelola hak akses dan izin pengguna dalam aplikasi. Ini memeriksa apakah pengguna memiliki izin yang sesuai untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu dalam aplikasi.
Dalam Django: Django memiliki sistem otorisasi yang kuat yang memungkinkan Anda untuk mengatur izin berdasarkan peran pengguna (roles), grup pengguna, dan izin kustom yang Anda tentukan. Anda dapat mengendalikan secara detail apa yang dapat diakses oleh setiap pengguna dalam aplikasi Anda.
Keduanya penting dalam konteks Django (dan dalam pengembangan aplikasi web umumnya) karena:

Keamanan: Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sementara otorisasi mengontrol apa yang dapat mereka lakukan setelah masuk. Ini penting untuk menjaga keamanan aplikasi Anda dan melindungi data pengguna.

Kepatuhan: Dalam beberapa aplikasi, terutama yang berhubungan dengan data sensitif atau peraturan privasi, Anda mungkin harus mematuhi persyaratan hukum atau peraturan yang mengharuskan Anda untuk memastikan bahwa hanya pengguna yang berhak yang dapat mengakses dan melakukan tindakan tertentu.

Pengalaman Pengguna: Otorisasi juga dapat digunakan untuk menciptakan pengalaman pengguna yang lebih personal, dengan memberikan hak akses berdasarkan peran dan kebutuhan pengguna.

Dengan menggunakan autentikasi dan otorisasi dengan benar dalam Django, Anda dapat membangun aplikasi web yang aman, terorganisir, dan sesuai dengan persyaratan bisnis atau regulasi yang berlaku.


 # Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
 Cookies adalah mekanisme penyimpanan data kecil yang digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien (pada peramban pengguna). Mereka digunakan untuk berbagai tujuan, termasuk mengelola sesi pengguna, melacak preferensi pengguna, dan menyimpan informasi sementara yang dapat digunakan kembali di seluruh sesi pengguna. Dalam konteks Django, cookies sering digunakan untuk mengelola data sesi pengguna.
Djanggo menggunakan cookies dengan:
1. Pengaturan Cookie Session: Pertama-tama, Anda perlu mengaktifkan dukungan sesi cookie dalam pengaturan Django Anda. Ini biasanya dilakukan dengan mengkonfigurasi SESSION_ENGINE dan SESSION_COOKIE_NAME dalam berkas settings.py
2. Penyimpanan Data Sesi: Ketika Anda ingin menyimpan data dalam sesi pengguna, Anda dapat menggunakan objek sesi Django. Ini memungkinkan Anda untuk menyimpan informasi seperti informasi login pengguna atau data kustom lainnya.
3. Penyimpanan Aman: Data dalam sesi pengguna akan disimpan dalam cookie sesi yang ditandatangani oleh Django. Ini berarti data tidak dapat dimanipulasi oleh pengguna, karena Django akan memeriksa integritas data sesi sebelum menggunakannya.
4. Pengambilan Data Sesi: Untuk mengambil data dari sesi pengguna, Anda dapat menggunakan sintaks yang mirip seperti yang digunakan saat menyimpan data.
5. Penutupan Sesi: Saat pengguna keluar atau sesi berakhir, Anda dapat menghapus data sesi dengan menggunakan perintah del atau pop. Setelah penghapusan data sesi, cookie sesi akan tetap ada di peramban pengguna, tetapi tidak akan berisi data.
 
# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat aman jika diimplementasikan dengan benar, tetapi ada beberapa risiko potensial yang harus diwaspadai. beberapa risiko dan masalah yang perlu dipertimbangkan: 
1. Kemungkinan Penyadapan
2. Masalah privasi
3. Cross-Site Scripting(XSS): Serangan XSS dapat menyebabkan pengeksekusian skrip berbahaya dalam konteks pengguna. Jika skrip ini dapat mengakses atau memodifikasi cookies pengguna, itu dapat membahayakan data pengguna.
4. Cross-Site Request Forgery(CSRF): Serangan CSRF dapat memanipulasi pengguna untuk melakukan tindakan tanpa sepengetahuan mereka. Jika cookies digunakan untuk otentikasi, serangan CSRF dapat menyebabkan tindakan berbahaya yang dilakukan atas nama pengguna.
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 Melakukan add-commit-push ke GitHub.

# BONUS
<img width="628" alt="Screen Shot 2023-09-26 at 20 04 08" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/f4ec9421-bb5e-4b44-84b0-ebe534dc65fe">
<img width="628" alt="Screen Shot 2023-09-26 at 20 03 54" src="https://github.com/sunflawlxs/PakBepeStore/assets/123561471/a958c372-c09d-4785-b24d-95b163abd064">


</details>



<details>
<summary> TUGAS 5</summary>
   
# Manfaat Element Selector
Element selector adalah bagian dari bahasa pemrograman CSS (Cascading Style Sheets) yang digunakan untuk memilih elemen HTML tertentu dan mendefinisikan gaya atau tampilan yang akan diterapkan pada elemen tersebut. Terdapat beberapa jenis selector yang berbeda dalam CSS, dan setiap jenis memiliki manfaat dan waktu yang tepat untuk digunakan. Berikut adalah penjelasan mengenai manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya:

Selector Universal (*):
Manfaat: Selector universal memilih semua elemen dalam dokumen HTML.
Waktu yang tepat: Digunakan dengan hati-hati karena dapat memengaruhi semua elemen dalam halaman. Biasanya digunakan untuk mereset atau mengatur nilai default untuk semua elemen.

Selector Elemen (Element Selector):
Manfaat: Selector elemen memilih semua elemen HTML dengan tag yang spesifik.
Waktu yang tepat: Digunakan ketika Anda ingin mengganti gaya atau tampilan semua elemen dengan tag yang sama dalam halaman.

Selector Kelas (Class Selector):
Manfaat: Selector kelas memilih semua elemen HTML yang memiliki atribut class tertentu.
Waktu yang tepat: Berguna ketika Anda ingin menerapkan gaya yang sama pada beberapa elemen yang memiliki kelas yang sama.

Selector ID (ID Selector):
Manfaat: Selector ID memilih elemen HTML yang memiliki atribut id tertentu.
Waktu yang tepat: Cocok untuk menerapkan gaya atau perilaku yang unik pada satu elemen tertentu dalam halaman. ID seharusnya unik dalam satu halaman.

<br>

# HTML5 Tag

| Tag | Penjelasan |
| --- | --- |
| `<a>` | Mendefinisikan hyperlink |
| `<abbr>` | Mendefinisikan bentuk singkatan dari kata atau frasa yang panjang |
| `<address>` | Menentukan informasi kontak penulis |
| `<area> `| Mendefinisikan area tertentu dalam peta gambar |
| `<!--...-->` | Menentukan komentar |
| `<!DOCTYPE>` | Menentukan jenis dokumen |
|` <div> `| Menentukan bagian dalam dokumen |
| `<detail>` | Menentukan informasi tambahan yang dapat diperoleh pengguna |
| `<header>` | Menentukan informasi tentang dokumen |
| `<q>` | Menentukan variabel |
| `<select>` | Menentukan daftar yang dapat dipilih |
| `<spacer>` | Menentukan white space |
| `<style>` | Menentukan definisi gaya |
| `<table>` | Menentukan tabel |

<br>

Source:
* https://www.tutorialrepublic.com/html-reference/html5-tags.php
* https://www.tutorialspoint.com/html5/html5_tags.htm
<br>

# Perbedaan Margin dan Padding 
Margin dan padding adalah dua properti dalam CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML, tetapi mereka memiliki peran yang berbeda dan diterapkan pada tempat yang berbeda dalam struktur elemen tersebut. Berikut adalah perbedaan antara margin dan padding:

Margin:
Margin adalah ruang di luar elemen: Margin adalah jarak antara batas elemen dan elemen-elemen di sekitarnya, seperti elemen-elemen tetangga atau batas kontainer. Margin digunakan untuk mengendalikan jarak antara elemen dan elemen lain di sekitarnya.
Tidak memiliki latar belakang atau warna: Margin tidak mempengaruhi latar belakang elemen atau warnanya. Ini adalah area transparan yang berfungsi sebagai "ruang kosong" di sekitar elemen.
Mengubah margin dapat memengaruhi tata letak elemen lain: Memperbesar margin suatu elemen dapat menggeser elemen-elemen tetangga yang berdekatan dengannya.

Padding:
Padding adalah ruang di dalam elemen: Padding adalah jarak antara batas elemen dan konten dalam elemen itu sendiri. Padding digunakan untuk mengendalikan jarak antara konten elemen dan batas elemen.
Pengaruh pada latar belakang atau warna: Padding akan memengaruhi latar belakang elemen dan warna elemen itu sendiri. Ketika padding diberikan, warna atau gambar latar belakang akan memperpanjang ke dalam padding area.
Mengubah padding tidak memengaruhi tata letak elemen lain: Memperbesar padding suatu elemen tidak akan mempengaruhi elemen-elemen tetangga. Ini hanya memengaruhi ruang di dalam elemen tersebut.


# Perbedan Tailwind CSS dan Bootstrap
Tailwind CSS dan Bootstrap adalah dua framework CSS populer yang digunakan untuk membangun tampilan web responsif dan estetis. Berikut adalah perbedaan antara keduanya dan kapan sebaiknya Anda menggunakan Bootstrap daripada Tailwind, dan sebaliknya:

Perbedaan antara Tailwind CSS dan Bootstrap:

Pendekatan Styling:

Tailwind CSS: Tailwind menggunakan pendekatan "utility-first", di mana Anda membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah ditentukan sebelumnya dalam CSS. Ini memungkinkan Anda untuk membuat tampilan yang sangat disesuaikan dengan menggabungkan kelas-kelas sesuai kebutuhan.
Bootstrap: Bootstrap menggunakan pendekatan "component-based", di mana komponen-komponen telah dirancang dan ditentukan sebelumnya. Anda menggunakannya dengan mengaitkan kelas-kelas yang telah ada ke elemen HTML.
Kustomisasi:

Tailwind CSS: Sangat fleksibel dan memungkinkan tingkat kustomisasi yang tinggi. Anda dapat dengan mudah menyesuaikan tampilan dengan mengedit konfigurasi atau menambahkan kelas-kelas utilitas khusus.
Bootstrap: Lebih terstruktur dan terbatas dalam hal kustomisasi. Untuk mengubah tampilan yang signifikan, Anda mungkin perlu menyesuaikan atau menimpa gaya Bootstrap yang ada.
Ukuran Kode:

Tailwind CSS: Hasil akhirnya dapat menghasilkan kode HTML yang lebih besar karena penggunaan banyak kelas utilitas. Namun, dengan teknik pengemasan (purging), Anda dapat menghilangkan kode yang tidak terpakai.
Bootstrap: Biasanya menghasilkan kode yang lebih ringkas karena penggunaan komponen yang telah dirancang sebelumnya. Namun, Anda mungkin hanya menggunakan sebagian kecil dari komponen Bootstrap yang tersedia.
Kapan sebaiknya Anda menggunakan Bootstrap daripada Tailwind, dan sebaliknya:

Bootstrap sebaiknya digunakan jika:

Anda memerlukan pengembangan cepat dan tidak ingin menghabiskan banyak waktu untuk menyesuaikan tampilan.
Anda bekerja dalam tim besar dan memerlukan pedoman yang jelas dalam hal tampilan dan interaksi.
Anda ingin menghindari kebingungan dalam memilih kelas-kelas utilitas dan lebih suka menggunakan komponen yang telah dirancang sebelumnya.
Anda memiliki pengalaman dengan Bootstrap atau tim Anda telah terbiasa menggunakannya.
Tailwind CSS sebaiknya digunakan jika:

Anda ingin tingkat kustomisasi yang tinggi dan tampilan yang sangat disesuaikan.
Anda lebih suka mengkode tampilan secara langsung dengan menggabungkan kelas-kelas utilitas.
Anda ingin menghindari kelebihan kode yang tidak terpakai dengan menggunakan teknik pengemasan.
Anda ingin mendekati tampilan dengan cara yang lebih alami, tanpa harus mengikuti gaya tertentu.
Kesimpulannya, pemilihan antara Bootstrap dan Tailwind CSS bergantung pada kebutuhan proyek Anda, tingkat kustomisasi yang diinginkan, dan preferensi Anda dalam pengembangan web. Keduanya memiliki kelebihan dan kelemahan masing-masing, dan tidak ada pilihan yang satu benar-benar lebih baik daripada yang lain dalam semua situasi.



## BONUS TUGAS 5**

1. Menambahkan style pada create_item.html, login.html, main.html, dan register.html direktori main.
2. Inventori di main.html ditampilkan menggunakan card
```<div class="product">
    {% for item in items %}
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">{{item.name}}</h5>
                <p class="card-text">{{item.description}}</p>
            </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item flex-v">Amount: {{item.amount}}
                    <div>
                        <a href="{% url 'main:add' item.id %}">
                            <button class="secondary-button">
                                Add
                            </button>
                        </a>
                        <a href="{% url 'main:remove' item.id %}">
                            <button class="secondary-button">
                                Remove
                            </button>
                        </a>
                    </div>
                </li>
                <li class="list-group-item">Price: {{item.price}}</li>
            </ul>
            <div class="card-body">
                <a href="{% url 'main:delete' item.id %}">
                    <button class="primary-button">Delete</button>
                </a>
            </div>
        </div>
    {% endfor %}
</div>
Mengerjakan bonus dengan menambahkan kode berikut di style main.html
.card:last-child, .card:last-child .flex-v {
    background: #1569C7;
}
```
Referensi: https://codepolitan.com/blog/perbedaan-bootstrap-dan-tailwind https://getbootstrap.com/docs/4.0/components/card/



</details>
