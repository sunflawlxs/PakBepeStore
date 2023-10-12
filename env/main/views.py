import datetime
import json

from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
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
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user) 

    context = {
        'app_name': 'main',
        'username': request.user.username,
        'class': 'PBP D',
        'products': products,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            messages.error(request, "Your username or password aren't valid!")
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

def get_item_json(request):
  Products = Product.objects.filter(user=request.user)
  return HttpResponse(serializers.serialize('json', Items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    product = Product.objects.get(pk=data["id"])
    product.delete()
    return HttpResponse("DELETED",status=200)

@csrf_exempt
def add_amount_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    product = Product.objects.get(pk=data["id"])
    product.amount += 1
    product.save()
    return HttpResponse(status=200)

@csrf_exempt
def remove_amount_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    product = Product.objects.get(pk=data["id"])
    if product.amount > 1:
        product.amount -= 1
        product.save()
    return HttpResponse(status=200)