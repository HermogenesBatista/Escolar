from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from escola.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Escolar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^escola/base', base),
    url(r'^escola/charts', graficos),
    url(r'^escola/forms', formularios),
    url(r'^escola/declaracao', declaracao),
    url(r'^escola/', index),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
