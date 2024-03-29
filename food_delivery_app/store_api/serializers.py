from rest_framework import serializers
from django.core.validators import validate_email
from .models import Store, Location, StoreEmail

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = "__all__"

class StoreEmailSerializer(serializers.ModelSerializer):
  email = serializers.EmailField()

  class Meta:
    model = StoreEmail
    fields = ['email']
  
  def to_internal_value(self, data):
    # data validation
    validate_email(data)
    if StoreEmail.objects.filter(email=data).exists():
      raise serializers.ValidationError(f'email: {data} is already in used. Please enter unique email.')
    return data

  def to_representation(self, instance):
    return instance.email

class StoreSerializer(serializers.HyperlinkedModelSerializer):
  location = LocationSerializer()
  emails = StoreEmailSerializer(many=True, allow_empty=False, max_length=3)
  menu_config = serializers.HyperlinkedIdentityField(view_name='menu-configuration-detail', lookup_url_kwarg='store_id')

  class Meta:
    model = Store
    depth = 1
    fields = [
      "url",
      "id",
      "name",
      "web_url",
      "avg_prep_time",
      "status",
      "timezone",
      "location",
      "emails",
      "menu_config"
    ]
  
  def create(self, validated_data):
    location_data = validated_data.pop('location')
    emails_data = validated_data.pop('emails')

    # create location
    location_instance = Location.objects.create(**location_data)
    # create store
    store_instance = Store.objects.create(**validated_data, location=location_instance)
    # bulk create emails
    emails = [StoreEmail(email=email_data, store=store_instance) for email_data in emails_data]
    StoreEmail.objects.bulk_create(emails)

    return store_instance

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