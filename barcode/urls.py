from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from manufacturing import views
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    path('manufacturing/', include("manufacturing.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
