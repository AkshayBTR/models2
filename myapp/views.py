from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from myapp.models import *
# Create your views here.
def response(request):
    return HttpResponse("<h1>Welcome to HttpResponse</h1>")


def  html_demo1(request):
    fruits={'fruit_name':["apple","banana","orange","pinapple"]}
    return render(request,"sample.html",context=fruits)


def  html_demo2(request):
    d={'data':"Django"}
    return render(request,"sample1.html",context=d)

def display_topics(request):
    data_topic=Webpage.objects.filter(Q(url__startswith="http:") & Q(url__endswith=".com/"))
    # data_webpage=Access_Details.objects.order_by('date')    
    # top={'topics':data_topic,"webpages":data_webpage}
    return render(request,"filter_demo.html",context={'Webpages':data_topic})