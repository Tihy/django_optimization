from django.conf.urls import url
import mainapp.views as mainapp
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


app_name = 'mainapp'
urlpatterns = [
    url(r'^$', mainapp.products, name='prod'),
    path('category/<pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),

    path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),


]