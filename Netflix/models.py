from django.db import models

# Create your models here.


# =================== USER ===================
class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)

# =================== MOVIES ===================


class Movies(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.CharField(max_length=50, null=False, default="")
    movieName = models.CharField(max_length=100,null=False,default="")
    kategoriId = models.BigIntegerField(null=False)
    etiketId = models.BigIntegerField(null=False)
    sure = models.CharField(max_length=50, null=False)
    puan = models.BigIntegerField()
    aciklama = models.TextField(max_length=500, null=False, default="")
    tarih = models.DateTimeField(auto_now_add=True)

    def get_image_path(self):
        return '/img1/flims/'+ self.image

    def get_movie_path(self):
        return '/video/'+ self.movieName

# =================== SERIES ===================


class Series(models.Model):
    name = models.CharField(max_length=50, null=False)
    image = models.CharField(max_length=50, null=False, default="")
    movieName = models.CharField(max_length=100,null=False,default="")
    kategoriId = models.BigIntegerField(null=False)
    etiketId = models.BigIntegerField(null=False)
    sure = models.CharField(max_length=50, null=False)
    puan = models.BigIntegerField()
    aciklama = models.TextField(max_length=500, null=False, default="")
    tarih = models.DateTimeField(auto_now_add=True)

# =================== CATEGORY ===================


class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=False)

# =================== MY FAVORITE ===================


class MyFavorite(models.Model):
    movieId = models.BigIntegerField(null=False)
    SeriesId = models.BigIntegerField(null=False)

# =================== MY FAVORITE MOVIES AND SERIES ===================


class MyFavoriteMoviesAndSeries(models.Model):
    movieId = models.BigIntegerField(null=False)
    SeriesId = models.BigIntegerField(null=False)

# =================== TICKET ===================


class Ticket(models.Model):
    ticketName = models.CharField(max_length=50, null=False)
