from django.urls import path,include
from . import views


path('',views.job_lists)
path('<int:id>',views.job_detail)