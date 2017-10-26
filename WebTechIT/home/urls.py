from home.views import index
from django.conf.urls import url
from home.views import\
     (
     index,
     post_detail_view,
     login_view,
     logout_view,
     register_user_view,
     add_comment,
     about_view
)
app_name = 'home'

urlpatterns = [
     url(r'^$', index, name='index'),
     url(r'^home/(?P<slug>[\w-]+)/$', post_detail_view, name='post-detail'),
     url(r'^home/(?P<slug>[\w-]+)/comments/$', add_comment, name='new-comment'),
     url(r'^login/$', login_view, name='login'),
     url(r'^logout/$', logout_view, name='logout'),
     url(r'^register/$', register_user_view, name='register'),
     url(r'^about/$', about_view, name='about')
]