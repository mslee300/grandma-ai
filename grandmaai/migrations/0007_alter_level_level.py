# Generated by Django 3.2.13 on 2023-03-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grandmaai', '0006_alter_level_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(blank=True, default='e', max_length=10),
        ),
    ]
