import datetime
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from main.models import Product
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    total_amount = Product.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount']
    jumlah_products = total_amount if total_amount is not None else 0  

    # if products:
    #     last_products = products.last()
    # else: 
    #     last_products = None


    context = {
        'AppName': 'PakBepeStore' ,
        'name': request.user.username,
        'class': 'PBP D', # Kelas PBP kamu
        'NPM': '2206824943',
        'products': products,
        'jumlah_products': str(jumlah_products),
        'last_login': request.COOKIES['last_login'],
      #  'last_products': last_products,
    }

    return render(request, "main.html", context)

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

def add_amount(request, id):
    try:
        products = Product.objects.get(pk=id)
        if request.method == 'GET':
            products.amount += 1
            products.save()
            messages.success(request, 'Sukses Menambah Amount.')
            return redirect('main:show_main')
        return redirect('main:show_main')
    except Product.DoesNotExist:
        raise Http404("Item tidak ditemukan.")
    
def remove_amount(request, id):
    try:
        products = Product.objects.get(pk=id)
        if request.method == 'GET':
            products.amount -= 1
            products.save()
            if products.amount == 0:
                products.delete()
            messages.success(request, 'Sukses Mengurangi Amount.')
            return redirect('main:show_main')
        return redirect('main:show_main')
    except Product.DoesNotExist:
        raise Http404("Item tidak ditemukan.")

def delete_product(request, id):
    try:
        products = Product.objects.get(pk=id)
        if request.method == 'GET':
            products.delete()
            messages.success(request, 'Sukses Menghapus Item.')
            return redirect('main:show_main')
        return redirect('main:show_main')
    except Product.DoesNotExist:
        raise Http404("Item tidak ditemukan.")
