"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from rest_framework import routers
# from quickstart import views
#
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
from hellow import views

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
from django.contrib import admin
from django.urls import include, path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hellow.urls')),
    url(r'^', include('snippets.urls')),
    url(r'^users/', views.users),
    url(r'^students/', views.StudentsView.as_view()),
    url(r'^order/', views.OrderView.as_view())

]