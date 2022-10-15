# Generated by Django 4.0.6 on 2022-09-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('category_image', models.ImageField(upload_to='category_pictures')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
