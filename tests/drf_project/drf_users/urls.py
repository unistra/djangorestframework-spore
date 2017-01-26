from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ListCreateUsers.as_view(), name='list_create_users'),
    url(r'^$', views.ListCreateSuperUsers.as_view(), name='list_create_super_users')
]
