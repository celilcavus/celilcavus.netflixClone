from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home),
    path('pages/home',views.Home),
    path('home',views.Index),
    path('login',views.SignIn,name='login'),
    path('register',views.Register,name='register'),
    path('home', views.logout, name= 'logout'),
    path('movies',views.Movies),
    path('favorite',views.favorite),
    path('search',views.search,name='search'),
    path('search/<str:name>',views.searchurl),
    path('moviesDetail/<int:id>',views.MoviesDetail),
    path('seriesDetail/<int:id>',views.SeriesDetail),
    path('series',views.Series),
]
