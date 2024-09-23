from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from .forms import UserForm
from django import forms


def index(request):
 return HttpResponse("<h2>Глaвнaя</h2>")

def about(request):
 return HttpResponse("<h2>0 сайте</h2>")

def contact(request):
 return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid):
 category = request.GET.get("cat", "")
 output = "<h2>Продукт № {0} Категория: {1}</h2>" .format(productid, category)
 return HttpResponse(output)
def users(request):
 id = request.GET.get("id", 1)
 name = request.GET.get("name", "Максим")
 output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} </h3 >" .format(id, name)
 return HttpResponse(output)

def index(request):
 return HttpResponse("Index")
def about(request):
 return HttpResponse("About")
def contact(request):
 return HttpResponseRedirect("/about")
def details(request):
 return HttpResponsePermanentRedirect("/")

def index(request):
 return render(request, "index.html")
def index(request):
 return render(request, "firstapp/home.html")

def index(request):
 data = {"header": "Передача параметров в шаблон Django",
 "message": "Загружен шаблон templates/firstapp/index_app1.html"}
 return render(request, "firstapp/index_app1.html", context=data)

def index(request):
 header = "Персональные данные" # обычная переменная
 langs = ["Английский", "Немецкий", "Испанский"] # массив
 user = {"name": "Максим,", "age": 30} # словарь
 addr = ("Виноградная", 23, 45) # кортеж
 data = {"header": header, "langs": langs, "user": user, "address": addr}
 return render(request, "index.html", context=data)

def index(request):
 header = "Персональные данные" # обычная переменная
 langs = ["Английский", "Немецкий", "Испанский"] # массив
 user = {"name": "Максим,", "age": 30} # словарь
 addr = ("Виноградная", 23, 45) # кортеж
 data = {"header": header, "langs": langs, "user": user, "address":
 addr}
 return TemplateResponse(request, "index.html", data)

def index(request):
 return render(request, "firstapp/home.html")

def index(request):
 return render(request, "firstapp/index.html")

def index(request):
 data = {"age": 77}
 return render(request, "firstapp/index.html", context=data)

def index(request):
 cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
 return render(request, "firstapp/index.html", context={"cat": cat})

def index(request):
 userform = UserForm()
 return render(request, "firstapp/index.html", {"form": userform})
class UserForm(forms.Form):
 file = forms.FileField(label="Файл")

