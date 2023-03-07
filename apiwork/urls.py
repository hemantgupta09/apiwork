from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from home.models import Login
from home.loginserializer import LoginSerializer
from home.Loginviewset import LoginViewset
router = routers.DefaultRouter()
router.register(r'logins', LoginViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
