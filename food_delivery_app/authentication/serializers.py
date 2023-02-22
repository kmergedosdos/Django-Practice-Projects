from .models import User
from rest_framework import serializers

class UserCreationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      'password'
    ]

  def validate(self, attrs):
    email_exists = User.objects.filter(email=attrs['email']).exists()
    if email_exists:
      raise serializers.ValidationError('email is already in used.')
    
    return super().validate(attrs)