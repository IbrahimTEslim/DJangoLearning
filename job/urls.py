from django.urls import path,include
from django.urls.resolvers import URLPattern
from . import views

app_name = 'job'

urlpatterns =  [
path('',views.job_lists,name='job_list'),
path('add',views.job_add,name='job_add'),
path('<str:slug>',views.job_details,name='job_detail'),
]