"""src URL Configuration

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
from rest_framework import routers
from .views import UserViewSet
# from allusers.views import AllUsersViewSet
# from posts.views import PostViewSet
# from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'allusers', AllUsersViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comments', include('comment.urls'))

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^', include('posts.urls')),
    url(r'^', include('comment.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
