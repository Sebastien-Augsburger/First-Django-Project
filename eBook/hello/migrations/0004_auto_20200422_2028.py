# Generated by Django 3.0.5 on 2020-04-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passengers', to='hello.Flight'),
        ),
    ]
