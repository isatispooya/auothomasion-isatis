# Generated by Django 5.0.6 on 2024-07-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='letter_number',
            field=models.IntegerField(),
        ),
    ]