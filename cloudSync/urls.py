from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^sync/', include('sync.urls')),
    #url(r'^(?P<username>\w+)/', include('sync.urls')),
    url(r'^admin/', admin.site.urls),
]
