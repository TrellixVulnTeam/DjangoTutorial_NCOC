# Generated by Django 2.0.3 on 2018-04-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
