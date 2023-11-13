from heros.views import *
from django.urls import path
app_name='rabel'

urlpatterns=[
    path('prabhas/',prabhas,name='prabhas'),
    path('ntr/',ntr,name='ntr'),
    

]