from heroine.views import *
from django.urls import path
app_name='cutie'

urlpatterns=[
    path('srinidhi/',srinidhi,name='srinidhi'),
    path('priyanka/',priyanka,name='priyanka'),
]