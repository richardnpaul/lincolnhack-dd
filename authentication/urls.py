from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, logout_then_login


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='logged_out.html'),
         name='logout'),
    path('logout-then-login/', logout_then_login,
        name='logout_then_login'),
    #url(r'^password-change/$', views.password_change,
    #    {'template_name': 'password_change_form.html'},
    #    name='password_change'),
    #url(r'^password-change/done/$', views.password_change_done,
    #    {'template_name': 'password_change_done.html'},
    #    name='password_change_done'),
]
