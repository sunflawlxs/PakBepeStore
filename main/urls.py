from main.views import show_main, create_product
from django.urls import path
from main.views import show_main
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import show_main, create_product, show_xml 
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user, delete_product, add_amount, remove_amount

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('create-product', create_product, name='create_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/<int:id>', add_amount, name='add'),
    path('remove/<int:id>', remove_amount, name='remove'),
    path('delete/<int:id>', delete_product, name='delete'),
]
