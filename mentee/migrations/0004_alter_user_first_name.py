# Generated by Django 5.0.2 on 2024-11-29 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0003_auto_20190508_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]