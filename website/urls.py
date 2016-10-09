from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.users_profile, name='profile'),
    url(r'^mp/(?P<mp_id>[\d]+)/$', views.mp_profile, name='mp'),
    url(r'^bills/$', views.bills, name='bills'),
]