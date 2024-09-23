from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return HttpResponse("<h2>Глaвнaя</h2>")

def about(request):
 return HttpResponse("<h2>0 сайте</h2>")

def contact(request):
 return HttpResponse("<h2>Koнтaкты</h2>")

def products(request, productid):
 output = "<h2>Продукт № {0}</h2>".format(productid)
 return HttpResponse(output)

def users(request, id=1, name="Данил"):
 output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} ".format(id,name)
 return HttpResponse(output)



