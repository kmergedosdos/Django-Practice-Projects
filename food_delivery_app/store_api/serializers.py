from rest_framework import serializers
from django.core.validators import validate_email
from .models import Store, Location, StoreEmail

# import pdb

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = "__all__"

class EmailListingField(serializers.StringRelatedField):  
  def to_internal_value(self, value):
    validate_email(value)
    if StoreEmail.objects.filter(email=value).__len__():
      raise serializers.ValidationError("This email already exists.")
    return value


class StoreSerializer(serializers.ModelSerializer):
  location = LocationSerializer()
  emails = EmailListingField(many=True)
  
  class Meta:
    model = Store
    depth = 1
    fields = [
      "id",
      "name",
      "web_url",
      "avg_prep_time",
      "status",
      "timezone",
      "location",
      "emails"
    ]
  
  def create(self, validated_data):
    location_data = validated_data.pop('location')
    emails_data = validated_data.pop('emails')

    if len(emails_data) < 1:
      raise serializers.ValidationError({'emails': "This field must not be empty."})
    
    location_instance = Location.objects.create(**location_data)
    store_instance = Store.objects.create(**validated_data, location=location_instance)
    
    for email in emails_data:
      StoreEmail.objects.create(email=email, store=store_instance)

    return store_instance
