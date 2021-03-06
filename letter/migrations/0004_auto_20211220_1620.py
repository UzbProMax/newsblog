# Generated by Django 3.2.9 on 2021-12-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_auto_20211217_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='letter.Tags'),
        ),
    ]
