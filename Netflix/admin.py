from django.contrib import admin

from Netflix import models

# Register your models here.

class SignInAdmin(admin.ModelAdmin):
    list_display = ('id','username','email')


class Movies(admin.ModelAdmin):
    list_display = ('id','name')

class Series(admin.ModelAdmin):
    list_display = ('id','name')

class Category(admin.ModelAdmin):
    list_display = ('id','categoryName')

class Favorite(admin.ModelAdmin):
    list_display = ('id','movieId','SeriesId')

class MyFavoriteMoviesAndSeries(admin.ModelAdmin):
    list_display = ('id','movieId','SeriesId')

class Ticket(admin.ModelAdmin):
    list_display = ('id','ticketName')



admin.site.register(models.User,SignInAdmin)
admin.site.register(models.Movies,Movies)
admin.site.register(models.Series,Series)
admin.site.register(models.Category,Category)
admin.site.register(models.MyFavorite,Favorite)
admin.site.register(models.MyFavoriteMoviesAndSeries,MyFavoriteMoviesAndSeries)
admin.site.register(models.Ticket,Ticket)