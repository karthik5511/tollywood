from villan.views import *
from django.urls import path
app_name='rudeboys'

urlpatterns=[
    path('jagapathi/',jagapathi,name='jagapathi'),
    path('rana/',rana,name='rana.html'),
]