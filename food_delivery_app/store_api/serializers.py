from rest_framework import serializers
from .models import Store, Location, StoreEmail

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = "__all__"


class StoreEmailSerializer(serializers.ModelSerializer):
  class Meta:
    model = StoreEmail
    fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Store
    depth = 1
    fields = [
      "id",
      "name",
      "location",
      "web_url",
      "avg_prep_time",
      "status",
      "timezone",
      "emails"
    ]
