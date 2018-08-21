from django.urls import path, reverse_lazy
from .views import register
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url

urlpatterns = [
    path('register/', register, name='register'),

    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, name='logout'),
    
    path('password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done'), 'template_name': 'accounts/password_reset_form.html'}, name='password_reset'),
    path('password-reset/done/', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete'), 'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('password-reset/complete/', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
]