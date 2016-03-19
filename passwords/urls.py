"""passwords URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from core.rest.views import register_endpoints as core_endpoints
from accounts.rest.views import register_endpoints, MyProfileEndpoint
from cypher.rest.views import register_endpoints as cypher_endpoint

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
register_endpoints(router)
core_endpoints(router)
cypher_endpoint(router)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-token/auth', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token/refresh', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api-token/verify', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/me/', MyProfileEndpoint.as_view()),
    url(r'^', include('passwords.core.urls'))
]
