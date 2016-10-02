"""histoslide_example URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from examples.views import home_page
from histoslide import urls as histo_urls

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^histoslide/',  include(histo_urls)),
]
