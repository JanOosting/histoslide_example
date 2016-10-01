"""histoslide_example URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from examples.views import home_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    # url(r'^admin/', admin.site.urls),
]
