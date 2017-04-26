from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views
from django.views import static
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files', views.FileViewSet, base_name = 'files')

app_name = 'sync'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    url('^', include('django.contrib.auth.urls')),
    url(r'^signup', views.addUser, name='signup'),
    url(r'^(?P<slug>[\w.@+-]+)/$', views.UserProfileView.as_view()),
]
