from home.loginserializer import LoginSerializer
from home.models import Login
from rest_framework import viewsets
class LoginViewset(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer