# Generated by Django 3.1.2 on 2021-11-23 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('emailid', models.EmailField(default='', max_length=40)),
                ('mobileno', models.IntegerField(default=0)),
                ('feedback', models.TextField(default='')),
            ],
        ),
    ]