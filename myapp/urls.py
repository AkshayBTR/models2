from django.urls import path
from myapp import views

app_name="myapp"

urlpatterns = [
    path('response/',views.response,name="response"),
    path('demo1/',views.html_demo1,name="demo1"),
    path('demo2/',views.html_demo2,name="demo2"),
    path("topics/",views.display_topics,name="topics"),
]
