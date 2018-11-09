from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
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
	if 'name' in request.POST:
		talker = request.POST['name']
		if 'msg' in request.POST:
			message = request.POST['msg']
			TextMessage.objects.create(talker = talker, message = message)
			msgs = TextMessage.objects.all()
			return render(request, 'guestbookver1.html',locals())

	
def login(request):
	if 'username' in request.POST:
		username = request.POST['username']
		if 'password' in request.POST:
			password = request.POST['password']
    #username = request.POST.get('usernamel', '')
    #password = request.POST.get('passwordl', '')
			print(username)
			print(password)
		    
			user = auth.authenticate(username=username, password=password)
			print(user)

			if user is not None:
				auth.login(request, user)
				return render(request, 'guestbookver1.html',locals())
			else:
				return HttpResponse('尚未登入')

def logout(request):
    auth.logout(request)
    return render(request, 'guestbookver1.html',locals())

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print("1")
            return HttpResponse('/guestbook/')
        else:
            form = UserCreationForm()
            print("2")
    return render(request, 'guestbook.html', {'form': form})

"""
def signup(request):
	if 'suname' in request.POST:
		susername = request.POST['suname']
		if 'spsw' in request.POST:
			spassword = request.POST['spsw']
			UserData.objects.create(username = susername, password = spassword)
	userdatas = UserData.objects.all()
	return HttpResponse("您已成功註冊")

def signin(request):
	userdatas = UserData.objects.all()
	msgs = TextMessage.objects.all()
	#suserdatas = UserData.objects.all()
	if 'uname' in request.POST:
		username = request.POST['uname']
		if 'psw' in request.POST:
			password = request.POST['psw']
			#signindata = str(username) + str(password)
			#userdatas = UserData.objects.all()
			username_c = UserData.objects.get(username = str(username))
			if username in username_c:
				return render(request, 'guestbookver1.html',locals())
			else:
				return HttpResponse("您尚未註冊或密碼錯誤")


...
def login(request):

    if request.user.is_authenticated(): 
        return render(request, 'guestbookver1.html',locals())

    username = request.POST['uname']
    password = request.POST['psw']
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return render(request, 'guestbookver1.html',locals())
    else:
        return HttpResponse("密碼錯誤")




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

