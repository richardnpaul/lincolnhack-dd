from django.conf.urls import url
from django.contrib.auth import views


urlpatterns = [
    url(r'^login/$', views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout,
        {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^logout-then-login/$', views.logout_then_login,
        name='logout_then_login'),
]
