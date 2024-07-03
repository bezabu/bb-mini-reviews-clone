# Generated by Django 4.1 on 2024-07-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0002_delete_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('color', models.SlugField(max_length=7)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]