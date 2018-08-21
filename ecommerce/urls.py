"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.static import serve
from django.conf import settings
from products.views import product_list, product_detail

from accounts.views import register
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/register/', register, name='register'),

    path('accounts/login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('accounts/logout/', logout, name='logout'),
    

    path('accounts/password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done'), 'template_name': 'accounts/password_reset_form.html'}, name='password_reset'),
    path('accounts/password-reset/done/', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete'), 'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('accounts/password-reset/complete/', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
    
    path('', product_list, name='product_list'),
    path('products/<id>', product_detail, name='product_detail'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
