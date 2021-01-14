from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hello(request):
     template = loader.get_template('hello.html')
     context = {}
     return HttpResponse(template.render(context))

def form_handler(request):
     template = loader.get_template('answer.html')
     if request.COOKIES.get('user_name') == None:
        name = request.POST.get('user_name')
        context = {'name': name}
        response = HttpResponse(template.render(context))
        response.set_cookie('user_name', name, 300)
        return response
     else:
        name = request.COOKIES['user_name']
        context = {'name': name}
        response = HttpResponse(template.render(context))
        return response


