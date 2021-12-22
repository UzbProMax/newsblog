# Generated by Django 3.2.9 on 2021-12-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='photos')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
    ]