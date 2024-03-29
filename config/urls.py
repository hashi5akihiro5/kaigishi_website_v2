from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#from accounts import views

#handler500 = views.my_customized_server_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('kakomon.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)