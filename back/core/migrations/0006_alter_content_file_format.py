# Generated by Django 4.1 on 2022-08-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_content_attach_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='file_format',
            field=models.CharField(choices=[('V', 'Video'), ('A', 'Audio'), ('D', 'Document'), ('I', 'Image')], max_length=1),
        ),
    ]
