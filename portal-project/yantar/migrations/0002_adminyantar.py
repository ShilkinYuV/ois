# Generated by Django 3.2 on 2021-05-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yantar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminyantar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.TextField(blank=True, null=True)),
                ('mail', models.TextField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'AdminYantar',
                'managed': False,
            },
        ),
    ]