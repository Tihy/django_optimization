import adminapp.views as adminapp
from django.urls import path
from django.conf.urls import url

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    url(r'^categories/create/$', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    url(r'^categories/read/$', adminapp.categories, name='categories'),
    url(r'^categories/update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    url(r'^categories/delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    url(r'^products/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
]