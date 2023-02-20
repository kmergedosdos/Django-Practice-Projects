from django.db import models

# Create your models here.
class Location(models.Model):
  address = models.CharField(max_length=50)
  address_2 = models.CharField(max_length=50)
  city = models.CharField(max_length=20)
  country = models.CharField(max_length=50)
  postal_code = models.CharField(max_length=10)
  state = models.CharField(max_length=50)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)

  def __str__(self) -> str:
    return f'{self.city}, {self.state}'

class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.OneToOneField(Location, on_delete=models.PROTECT)
  web_url = models.CharField(max_length=100)
  avg_prep_time = models.IntegerField()
  status = models.CharField(max_length=50)
  timezone = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class StoreEmail(models.Model):
  email = models.EmailField(unique=True)
  store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="emails")

  def __str__(self):
    return self.email