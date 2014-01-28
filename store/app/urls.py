from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<url_category_name>\w+)/$', views.category, name='category'),
        url(r'^category/(?P<url_category_name>\w+)/add_item/$', views.add_item, name='add_item' ),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^goto/$', views.track_url, name='track_url'),
        url(r'^like_category/$', views.like_category, name='like_category'),
    )
