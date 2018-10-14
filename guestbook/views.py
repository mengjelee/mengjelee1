from django.shortcuts import render

# Create your views here.
def guestbook_list(request):
	return render(request,'guestbook.html')
	#不要在guestbook.html前加guestbook/來指定位置