# Generated by Django 4.2.2 on 2023-06-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_remove_author_author_name_author_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('CRIME', 'Crime'), ('FANTASY', 'Fantasy'), ('MYSTERY', 'Mystery'), ('ROMANCE', 'Romance'), ('SCI-FI', 'Sci-Fi')], max_length=7),
        ),
    ]
