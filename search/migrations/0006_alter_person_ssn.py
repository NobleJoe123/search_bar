# Generated by Django 5.0.9 on 2024-10-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_alter_person_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='ssn',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
