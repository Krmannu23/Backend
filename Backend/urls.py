"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,include
from rest_framework.schemas import get_schema_view 
from django.views.generic import TemplateView 
from Application import views
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.routers import DefaultRouter

authRouter=DefaultRouter(trailing_slash=False)

authRouter.register(r'userList' ,views.UserListViewSet ,basename="lists")
urlpatterns = [
    path('admin/', admin.site.urls),#mannu 123mannu
    path(r'authUserList/',include(authRouter.urls)),
    path('createUser',views.CreateUserView.as_view() ,name='create_user'), 
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'), #refresh + access
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('application/user',include("Application.urls")),
    path('studentapi', get_schema_view(
        title="Service",
        description="Student API "
    ), name='openapi-schema'),
     path('docs/', TemplateView.as_view(
        template_name='ApiDocumentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

if settings.DEBUG: #for development environment enable debugging
    import debug_toolbar
    urlpatterns+= path("__debug__/", include("debug_toolbar.urls")),