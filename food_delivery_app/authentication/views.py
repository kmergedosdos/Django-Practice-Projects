from rest_framework import generics

from .models import User
from .serializers import UserCreationSerializer

# Create your views here.
class UserCreationView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserCreationSerializer