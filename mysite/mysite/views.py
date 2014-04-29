# -*- coding: utf-8 -*-  
from django.http import HttpResponse
from django.template import Template, Context  # 记住导入
from django.template.loader import get_template  # 记得导入
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib import auth  
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.utils.translation import ugettext_lazy as _
from forms import RegisterForm, LoginForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method =='GET':
        if request.user.is_authenticated():
            t = get_template('logon-index.html')
            c = Context({'user_name':request.user.get_username()})
            html = t.render(c)
            return HttpResponse(html)
        else:
            t = get_template('index.html')
            c = Context({})
            html = t.render(c)
            return HttpResponse(html)
    else:
        form = LoginForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username', '')  
            password = request.POST.get('password', '')  
            user = auth.authenticate(username=username, password=password)  
            if user is not None and user.is_active:  
                auth.login(request, user)  
                return render_to_response('logon-index.html', context_instance=RequestContext(request))  
            else:
               return render_to_response('index.html', context_instance=RequestContext(request, {'form': form,'password_is_wrong':True}))  
        else:  
            return render_to_response('index.html', context_instance=RequestContext(request, {'form': form,}))  


def news(request):
    if request.user.is_authenticated():
        t = get_template('news.html')
        c = Context({})
        html = t.render(c)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('../')

def sfile(request):
   if request.user.is_authenticated():
        t = get_template('sfile.html')
        c = Context({})
        html = t.render(c)
        return HttpResponse(html)
   else:
     return HttpResponseRedirect('../')


def tfile(request):
    if request.user.is_authenticated():
        t = get_template('tfile.html')
        c = Context({})
        html = t.render(c)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('../')

def update(request):
    if request.user.is_authenticated():
        t = get_template('update.html')
        c = Context({})
        html = t.render(c)
        return HttpResponse(html)
    else:
        return HttpResponseRedirect('../')

def logout(request):
    logout(request)
    t = get_template('index.html')
    c = Context({})
    html = t.render(c)
    return HttpResponse(html)

def loginError(): 
    #如果没有登录并试图访问页面
        t = get_template('index.html')
        c = Context({})
        html = t.render(c)
        return HttpResponse(html)


    
    

