from django.urls import path
from . import views



app_name='desktop'
urlpatterns=[

	path('',views.index, name='home'),

]