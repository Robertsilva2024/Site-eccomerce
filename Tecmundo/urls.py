from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
# Certifique-se de que Payment está importado corretamente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

