from django.db import models

from store_api.models import Store

# Create your models here.
class MenuConfig(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name="menu_config")

    def __str__(self) -> str:
        return f'MenuConfig {self.store.name}'
    
    class Meta:
        verbose_name = "Menu Configuration"
        verbose_name_plural = "Menu Configurations"

class Category(models.Model):
    menu_config = models.ForeignKey(MenuConfig, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"

class Menu(models.Model):
    menu_config = models.ForeignKey(MenuConfig, on_delete=models.CASCADE, related_name='menus')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category, blank=True, related_name='menus')

    def __str__(self) -> str:
        return self.title

class Item(models.Model):
    menu_config = models.ForeignKey(MenuConfig, on_delete=models.CASCADE, related_name='items')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300, blank=True)
    image_url = models.URLField(max_length=300, blank=True)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    