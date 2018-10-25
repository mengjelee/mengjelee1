from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random
from django import template
from django.template.loader import get_template 
from guestbook.models import TextMessage
from guestbook.models import UserData


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
			userdatas = UserData.objects.all()
			return render(request, 'guestbookver1.html',locals())
	if 'uname' in request.POST:
		username = request.POST['uname']
		if 'psw' in request.POST:
			password = request.POST['psw']
			#signindata = str(username) + str(password)
			#userdatas = UserData.objects.all()	
			if username == str(123):
				if password == str(456):
					msgs = TextMessage.objects.all()
					userdatas = UserData.objects.all()
					return render(request, 'guestbookver1.html',locals())
				else:
					return HttpResponse("密碼錯誤")
			else:
				return HttpResponse("您尚未註冊")
	

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
			if username == str(123):
				if password == str(456):
					return render(request, 'guestbookver1.html',locals())
				else:
					return HttpResponse("密碼錯誤")
			else:
				return HttpResponse("您尚未註冊")

"""
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

