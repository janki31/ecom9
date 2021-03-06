# Generated by Django 3.1.2 on 2021-12-04 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('blogid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('desc', models.TextField(default='')),
                ('head0', models.CharField(default='', max_length=20)),
                ('chead0', models.CharField(default='', max_length=1500)),
                ('head1', models.CharField(default='', max_length=20)),
                ('chead1', models.CharField(default='', max_length=1500)),
                ('head2', models.CharField(default='', max_length=20)),
                ('chead2', models.CharField(default='', max_length=1500)),
                ('pub_date', models.DateField(default='')),
                ('image_file', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
