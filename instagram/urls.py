from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$',views.home,name='home'),
   url(r'^profile/profile/(\d+)',views.profile,name = 'profile'),
   url(r'^image/$', views.add_image, name='upload_image'),
   url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
   url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    
]




if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)