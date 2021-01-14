from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def hello(request):
     template = loader.get_template('hello.html')
     context = {}
     return HttpResponse(template.render(context))

def form_handler(request):
     template = loader.get_template('answer.html')
     if request.session.get('user_name') == None:
        name = request.POST.get('user_name')
        request.session['user_name'] = name
        context = {'name': name}
        response = HttpResponse(template.render(context))
        return response
     else:
        name = request.session.get('user_name')
        context = {'name': name}
        response = HttpResponse(template.render(context))
        return response


