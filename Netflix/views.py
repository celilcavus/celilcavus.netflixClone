from django.shortcuts import get_object_or_404, redirect, render
from .models import Movies as m, Series as s, User, MyFavorite as fv
from django.contrib.auth.models import User
from django.contrib import auth, messages
# Create your views here.
username = ""


def Home(request):
    moviesValue = m.objects.all()
    SeriesValue = s.objects.all()
    Users = username
    url = {
        'movie': moviesValue,
        'serie': SeriesValue,
        'user': Users
    }
    return render(request, 'pages/home.html', url)


def Movies(request):
    moviesValue = m.objects.all()
    url = {
        'movie': moviesValue,
    }
    return render(request, 'Movies.html', url)


def MoviesDetail(request, id):
    FindMovieAndSeries = get_object_or_404(m, pk=id)
    moviesValue = m.objects.all()
    SeriesValue = s.objects.all()
    url = {
        'movie': moviesValue,
        'series': SeriesValue,
        'findMovie': FindMovieAndSeries
    }
    return render(request, 'MovieAndSeries.html', url)


def Series(request):
    moviesValue = m.objects.all()
    url = {
        'movie': moviesValue,
    }
    return render(request, 'Series.html', url)


def SeriesDetail(request, id):
    return render(request, 'MovieAndSeries.html')


def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('login başarılı')
            return redirect('/')
        else:
            print('kullanıcı adı veya parola yanlış')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Register(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if (User.objects.filter(username=username).exists()):
            messages.add_message(request, messages.WARNING,
                                 'Bu User Name Daha onceden alinmiş')
            return redirect('register')
        else:
            if (User.objects.filter(email=email).exists()):
                messages.add_message(
                    request, messages.WARNING, 'Bu email daha önce alinmiş')
                return redirect('register')
            else:
                # her şey güzel
                user = User.objects.create_superuser(
                    username=username, password=password, email=email)
                user.save()
                messages.add_message(request, messages.INFO,
                                     'Kullanici Oluşturuldu.')
                return redirect('login')
    return render(request, 'register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS,
                             'Oturumunuz kapatıldı.')
        return redirect('home')


def Index(req):
    return render(req, 'home.html')


def favorite(req):
    favoritevalue = fv.objects.get(5)
    # favoritevalue.query.as_sql("SELECT * FROM Movies Where id = 5")
    fav = {
        'myfavorite': favoritevalue
    }
    return render(req, 'favorite.html')


def search(request):
    if request.method == "POST":
        name = request.POST['name']
        getmovie = m.objects.filter(name=name)
        url = {
            'movie': getmovie
        }
        return render(request, 'search.html', url)
    else:
        return redirect('/')


def searchurl(request, name):
    getmovie = m.objects.filter(name=name)
    url = {
        'movie': getmovie
    }
    return render(request, 'search.html', url)

