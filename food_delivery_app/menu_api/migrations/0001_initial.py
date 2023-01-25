# Generated by Django 4.1.4 on 2023-01-20 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store_api', '0005_alter_store_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='menu_config', to='store_api.store')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('categories', models.ManyToManyField(to='menu_api.menuconfig')),
                ('menu_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='menu_api.menuconfig')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('menu_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='menu_api.menuconfig')),
            ],
        ),
    ]