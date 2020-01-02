
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
app_name = 'core'
urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include(('core.urls', 'core'), namespace='core')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)