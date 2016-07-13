from django.conf.urls import url
from . import views


app_name = 'chat'
urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='index'),
    url(r'^send/$', views.MessageCreate.as_view(), name='send'),
    #url(r'^inbox/$', views.InboxView.as_view(), name='inbox'),
    #url(r'^inbox/$', views.inboxview1, name='inbox'),
    url(r'^signin/$', views.SignIn.as_view(), name='signin')
]