# Generated by Django 5.0.3 on 2024-03-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticuloBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='imagenes-blog')),
                ('slug_article', models.SlugField(max_length=90)),
                ('date_created', models.DateField(auto_now=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
