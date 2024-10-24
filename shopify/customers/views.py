from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func1(request,id,user1,product,cardno,phoneno):
    return HttpResponse('id':1,'user1':'Zara','product':'wallet','cardno':23000,'phoneno':77804)
    
