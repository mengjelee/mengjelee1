from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponseRedirect
import random
from django import forms
from django import template
from django.template.loader import get_template 
from guestbook.models import TextMessage
from guestbook.models import UserData
from django.contrib.auth.forms import UserCreationForm

def index(request):	
	#t1 = TextMessage.objects.create(talker = "will", message = "imwill")
	#t2 = TextMessage.objects.create(talker = "jennifer", message = "imjen")
	#t3 = TextMessage.objects.create(talker = "tim", message = "iamnobody")
	talker = request.user
	if 'msg' in request.POST:
		message = request.POST['msg']
		TextMessage.objects.create(talker = talker, message = message)
	msgs = TextMessage.objects.all()
	return render(request, 'guestbookver1.html',locals())

def login(request):
    msgs = TextMessage.objects.all()
    if request.user.is_authenticated: 
        #print("t1")
        return render(request, 'guestbookver1.html',locals())
    if request.method == 'POST':
        if 'username' in request.POST:
            #print("t2")
            username = request.POST['username']
            if 'password' in request.POST:
                password = request.POST['password']
                user = auth.authenticate(username=username, password=password)
                auth.login(request,user)
                #print("8")
                if user is not None:
                    if user.is_active:
                        auth.login(request,user)
                        print("成功登入")
                    else:
                       return HttpResponse('尚未登入')
                else:
                   return HttpResponse('登入失敗!')
    return render(request, 'guestbookver1.html',locals())
def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            if 'password' in request.POST:
                password = request.POST['password']
                if 'email' in request.POST:
                    email = request.POST['email']
                    #form = UserCreationForm(request.POST)
                    print("0")
                    try:
                        user = User.objects.get(username=username)
                    except:
                        user = None
                        print("user is None")
                    if user is None:
                        user = User.objects.create_user(username,email, password)
                        user.save()
                        message = "註冊成功"
                        print("3")
                    else:
                        message = '此使用者已經有人使用'
                        print("4")                  
    return render(request, 'guestbook.html',locals())

def personalpage(request):
    if request.user.is_authenticated:
        sender = request.user
    else:
        message="你尚未登入"
    if 'update' in request.POST:
        #idex=request.POST['idex']
        sender=request.POST['sender']
        newtalk=request.POST['newtalk']
        talk=request.POST['talk']
        TextMessage.objects.filter(talker=sender,message=talk).update(message=newtalk)
    if 'delete' in request.POST:
        #idex=request.POST['idex']
        sender=request.POST['sender']
        talk=request.POST['talk']
        TextMessage.objects.filter(talker=sender,message=talk).delete()
    if 'search' in request.POST:
        talk=request.POST['talk']
        sender=request.POST['sender']
        conversation=TextMessage.objects.filter(message__icontains=talk,talker=sender)
        return render(request,'personalpage.html',locals())
    conversation=TextMessage.objects.filter(talker=sender)
    return render(request,'personalpage.html',locals())


"""
隨機圖片碼
random.seed('foobar')     # 設定 random seed

def index(request):
	templates = get_template('guestbookver1.html')
	urllist = []
	for i in range(30):
		url = ""
		ori_url = "https://picsum.photos/200/200?image="
		a = random.randint(100, 900)
		url = ori_url+str(a)
		urllist.append(url)
		context = { "urllist" : urllist}
	return render(request, 'guestbookver1.html',context) #一定要按照順序
"""

