# Generated by Django 3.2.2 on 2021-05-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anons_field', models.CharField(max_length=300)),
                ('image_field', models.ImageField(upload_to='')),
            ],
        ),
    ]
