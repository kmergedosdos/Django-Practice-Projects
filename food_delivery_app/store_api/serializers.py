from rest_framework import serializers
from django.core.validators import validate_email
from .models import Store, Location, StoreEmail

from django.db import IntegrityError

# import pdb

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = "__all__"

class StoreEmailSerializer(serializers.ModelSerializer):
  email = serializers.EmailField()

  class Meta:
    model = StoreEmail
    fields = ['email']

class StoreSerializer(serializers.ModelSerializer):
  location = LocationSerializer()
  emails = StoreEmailSerializer(many=True, allow_empty=False, max_length=3)
  
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

    # check if email already exists in the db
    for email_data in emails_data: 
      email = email_data.get('email', '')
      if StoreEmail.objects.filter(email=email).__len__():
        raise serializers.ValidationError(f"emails: [{email} already exists.]")
    
    location_instance = Location.objects.create(**location_data)
    store_instance = Store.objects.create(**validated_data, location=location_instance)
    
    for email_data in emails_data:
      email = email_data.get('email', '')
      StoreEmail.objects.create(email=email, store=store_instance)

    return Store.objects.last()

  def update(self, instance, validated_data):
    location_data = validated_data.pop('location')
    emails_data = validated_data.pop('emails')

    for email_data in emails_data:
      # save email if it does not exist yet in the db
      StoreEmail.objects.get_or_create(email=email_data.get('email'), store=instance)
      
    # update instance
    instance.name = validated_data.get('name', instance.name)
    instance.web_url = validated_data.get('web_url', instance.web_url)
    instance.avg_prep_time = validated_data.get('avg_prep_time', instance.avg_prep_time)
    instance.status = validated_data.get('status', instance.status)
    instance.timezone = validated_data.get('timezone', instance.timezone)
    instance.save()
    
    # update location of the instance
    location = instance.location
    location.address = location_data.get('address', location.address)
    location.address_2 = location_data.get('address_2', location.address_2)
    location.city = location_data.get('city', location.city)
    location.country = location_data.get('country', location.country)
    location.postal_code = location_data.get('postal_code', location.postal_code)
    location.state = location_data.get('state', location.state)
    location.latitude = location_data.get('latitude', location.latitude)
    location.longitude = location_data.get('longitude', location.longitude)
    location.save()

    return instance