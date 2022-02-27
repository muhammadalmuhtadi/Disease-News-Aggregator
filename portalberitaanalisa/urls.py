from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('portalberita.urls')),
    path('scrapereport/', include('scrapereport.urls')),
    path('analisa/', include('analisa.urls')),
    #path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
