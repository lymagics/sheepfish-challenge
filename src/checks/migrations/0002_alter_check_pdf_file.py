# Generated by Django 4.1.7 on 2023-03-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='pdf_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]