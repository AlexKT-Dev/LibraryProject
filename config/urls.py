from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Подключение медиа каталога
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
