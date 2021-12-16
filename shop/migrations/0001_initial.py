# Generated by Django 3.1.2 on 2021-11-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=30)),
                ('product_desc', models.TextField(default='')),
                ('product_price', models.IntegerField(default=0)),
                ('pub_date', models.DateField()),
                ('product_image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]