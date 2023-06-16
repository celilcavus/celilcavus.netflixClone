# Generated by Django 3.2.4 on 2023-06-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kategoriId', models.BigIntegerField()),
                ('etiketId', models.BigIntegerField()),
                ('sure', models.CharField(max_length=50)),
                ('puan', models.BigIntegerField()),
                ('aciklama', models.TextField(default='', max_length=500)),
                ('tarih', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.BigIntegerField()),
                ('SeriesId', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyFavoriteMoviesAndSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.BigIntegerField()),
                ('SeriesId', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('kategoriId', models.BigIntegerField()),
                ('etiketId', models.BigIntegerField()),
                ('sure', models.CharField(max_length=50)),
                ('puan', models.BigIntegerField()),
                ('aciklama', models.TextField(default='', max_length=500)),
                ('tarih', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketName', models.CharField(max_length=50)),
            ],
        ),
    ]