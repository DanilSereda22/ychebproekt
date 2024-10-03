from django.http import *
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from .forms import UserForm
from django import forms
from .models import Person


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
 if request.method == "POST":
  name = request.POST.get("name") # получить значения поля Имя
  age = request.POST.get("age") # значения поля Возраст
  output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст – {1}</h3>".format(name, age)
  return HttpResponse(output)
 else:
  userform = UserForm()
  return render(request, "firstapp/index.html", {"form": userform})

def index(request):
 people = Person.objects.all()
 return render(request, "index.html", {"people": people})
# сохранение данных в БД
def create(request):
 if request.method == "POST":
  klient = Person()
  klient.name = request.POST.get("name")
  klient.age = request.POST.get("age")
  klient.save()
 return HttpResponseRedirect("/")

# получение данных из БД и загрузка index.html
def index(request):
 people = Person.objects.all()
 return render(request, "index.html", {"people": people})
# сохранение данных в БД

# сохранение данных в БД
def create(request):
 if request.method == "POST":
  klient = Person()
  klient.name = request.POST.get("name")
  klient.age = request.POST.get("age")
  klient.save()
 return HttpResponseRedirect("/")

# изменение данных в БД
def edit(request, id):
 try:
     person = Person.objects.get(id=id)

     if request.method == "POST":
      person.name = request.POST.get("name")
      person.age = request.POST.get("age")
      person.save()
      return HttpResponseRedirect("/")
     else:
      return render(request, "edit.html", {"person": person})
 except Person.DoesNotExist:
     return HttpResponseNotFound("<h2>Клиент не найден</h2>")
# удаление данных из БД
def delete(request, id):
  try:
   person = Person.objects.get(id=id)
   person.delete() 
   return HttpResponseRedirect("/")
  except Person.DoesNotExist:
   return HttpResponseNotFound("<h2>Клиент не найден</h2>")