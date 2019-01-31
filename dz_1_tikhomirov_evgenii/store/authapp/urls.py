from django.conf.urls import url
import authapp.views as authapp
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'authapp'
urlpatterns = [

    url(r'^login/$', authapp.login, name='login'),
    url(r'^logout/$', authapp.logout, name='logout'),
    url(r'^register/$', authapp.register, name='register'),
    url(r'^edit/$', authapp.edit, name='edit'),
    path ('verify/<str:email>/<str:active_key>',authapp.verify, name='verify')
]