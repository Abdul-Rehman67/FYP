# Generated by Django 2.2.10 on 2021-03-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customized'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='document',
            field=models.FileField(default='sen1.xml', upload_to='documents/%Y/%m/%d'),
        ),
    ]
