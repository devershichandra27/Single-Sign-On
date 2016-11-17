from django.conf.urls import url
from . import views


app_name = 'chat'
urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='index'),
    url(r'^app2/$', views.app2, name='app2'),
    url(r'^app1/$', views.app1, name='app1'),
    url(r'^logout/$', views.logoutview, name='logout'),
    url(r'^signin/$', views.SignIn.as_view(), name='signin')
]
