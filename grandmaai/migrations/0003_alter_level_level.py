# Generated by Django 3.2.13 on 2023-03-28 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandmaai', '0002_auto_20230328_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(default='e', max_length=10),
        ),
    ]
