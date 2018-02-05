from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^posts/$', views.post_list, name="post_list"),
    url(r'^posts/details/(?P<id>[\d]+)/$',views.post_details, name="details")
]
