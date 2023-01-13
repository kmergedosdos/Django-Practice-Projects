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

    # explicitly require email field
    if len(emails_data) < 1:
      raise serializers.ValidationError({'emails': "This field must not be empty."})

    # check if email already exists in the db
    for email in emails_data: 
      if StoreEmail.objects.filter(email=email).__len__():
        raise serializers.ValidationError(f"emails: {email} already exists.")
    
    location_instance = Location.objects.create(**location_data)
    store_instance = Store.objects.create(**validated_data, location=location_instance)
    
    for email in emails_data:
      StoreEmail.objects.create(email=email, store=store_instance)

    print('create')

    return store_instance

  def update(self, instance, validated_data):
    location_data = validated_data.pop('location')
    emails_data = validated_data.pop('emails')
    
    print("\n\n instance emails", instance.emails.all())

    for email in emails_data:
      # save email if it does not exist yet in the db
      StoreEmail.objects.get_or_create(email=email, store=instance)
      

    print("location", location_data.get('address'))

    instance.name = validated_data.get('name', instance.name)
    instance.web_url = validated_data.get('web_url', instance.web_url)
    instance.avg_prep_time = validated_data.get('avg_prep_time', instance.avg_prep_time)
    instance.status = validated_data.get('status', instance.status)
    instance.timezone = validated_data.get('timezone', instance.timezone)
    instance.location.address = location_data.get('address', instance.location.address)
    instance.location.address_2 = location_data.get('address_2', instance.location.address_2)
    instance.location.city = location_data.get('city', instance.location.city)
    instance.location.country = location_data.get('country', instance.location.country)
    instance.location.postal_code = location_data.get('postal_code', instance.location.postal_code)
    instance.location.state = location_data.get('state', instance.location.state)
    instance.location.latitude = location_data.get('latitude', instance.location.latitude)
    instance.location.longitude = location_data.get('longitude', instance.location.longitude)
    instance.location.save()
    instance.save()

    return instance