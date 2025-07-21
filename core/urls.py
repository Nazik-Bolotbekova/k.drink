
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Главная страница проекта</h1>")

urlpatterns = [
    path('',home_view),
    path('admin/', admin.site.urls),
    path('drinks/',include('apps.drinks.urls')),
    path('users/',include('apps.users.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
