# Generated by Django 3.1.7 on 2021-04-17 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrudUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
