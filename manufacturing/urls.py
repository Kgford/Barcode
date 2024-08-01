from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from manufacturing.views import (
    BarcodeView,
)

app_name = "manufacturing"

urlpatterns =[
   path('barcode_view/', BarcodeView.as_view(template_name="barcode_view.html"), name='barcode_view'),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

 
