from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random
from django import template
from django.template.loader import get_template 
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

