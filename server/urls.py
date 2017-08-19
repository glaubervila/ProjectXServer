"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from common import routers
from advertising.urls import router as advertising_router

router = routers.DefaultRouter()
router.extend(advertising_router)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api'))
]


# Adiciona a url de Rest Framework browsable API somente em ambientes de develop and test.
if settings.DEBUG:
    # Additionally, we include login URLs for the browsable API
    urlpatterns.append(
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    )
