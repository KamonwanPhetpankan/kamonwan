# Generated by Django 2.2.6 on 2019-10-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]