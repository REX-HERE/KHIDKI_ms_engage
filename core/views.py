import os
from collections import defaultdict
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.forms import ProfileForm
from .bag_of_words import Recommend_bow
from .constants import Debug
from .bert import Fetch_poster, Recommend
from .models import Movie, Profile, Dropdown



class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/profile/')
        return render(request, 'index.html')


@method_decorator(login_required, name='dispatch')
class ProfileList(View):

    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()

        print(profiles)

        return render(request, 'profileList.html', {
            'profiles': profiles
        })


@method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()

        return render(request, 'profileCreate.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect(f'/watch/{profile.uuid}')

        return render(request, 'profileCreate.html', {
            'form': form
        })


@method_decorator(login_required, name='dispatch')
class Watch(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)

            class Showcase:
                def __init__(self, a, b, c):
                    self.movie_id = a
                    self.movie_title = b
                    self.posterLink = c

            if profile.age_limit == 'Kids':
                try:
                    # showcase = movies_age[0]
                    showcase = Movie.objects.get(title='Harry Potter and the Philosopher\'s Stone')
                    poster = Fetch_poster(showcase.movie_id)
                except:
                    showcase = None

                movies_list1 = []
                movies_list2 = []
                temp_movie = Movie.objects.get(title='Jurassic Park III')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Stuart Little')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Jurassic Park')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Stuart Little 2')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))

                temp_movie = Movie.objects.get(title='Toy Story')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Toy Story 3')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='The Adventures of Elmo in Grouchland')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Stitches')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))


            else:
                try:
                    # showcase = movies_age[0]
                    showcase = Movie.objects.get(title='Avengers: Age of Ultron')
                    poster = Fetch_poster(showcase.movie_id)
                except:
                    showcase = None

                movies_list1 = []
                movies_list2 = []
                temp_movie = Movie.objects.get(title='Avatar')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Harry Potter and the Philosopher\'s Stone')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Jurassic Park')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='The Shawshank Redemption')
                movies_list1.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))

                temp_movie = Movie.objects.get(title='The Dark Knight Rises')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='Interstellar')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='The Dictator')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))
                temp_movie = Movie.objects.get(title='The Social Network')
                movies_list2.append(Showcase(temp_movie.movie_id, temp_movie.title, Fetch_poster(temp_movie.movie_id)))



            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            return render(request, 'movieList.html', {
                # 'profile': profile,
                'showcase': showcase,
                'poster': poster,
                'age_limit': profile.age_limit,
                'movies_list1': movies_list1,
                'movies_list2': movies_list2
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')


@method_decorator(login_required, name='dispatch')
class ShowMovieDetail(View):
    print("arrive")
    def get(self, request, movie_id, age_limit, *args, **kwargs):
        try:
            movie_called = Movie.objects.get(movie_id=movie_id)
            poster = Fetch_poster(movie_called.movie_id)

            movie_recommendation_bow = Recommend_bow(movie_called.title)
            movie_recommendation = Recommend(movie_called.title)

            class MovieObj:
                def __init__(self, a, b, c):
                    self.movie_id = a
                    self.movie_title = b
                    self.posterLink = c

            if age_limit == 'Kids':
                rec_movies_bow = []
                for id_bow in movie_recommendation_bow:
                    try:
                        temp = Movie.objects.get(age_limit=age_limit, movie_id=id_bow)
                        rec_movies_bow.append(temp)
                    except Movie.DoesNotExist:
                        pass

                rec_movies = []
                for id in movie_recommendation:
                    try:
                        temp = Movie.objects.get(age_limit=age_limit, movie_id=id)
                        if temp not in rec_movies_bow:
                            rec_movies.append(temp)
                    except Movie.DoesNotExist:
                        pass
                movies_list = []
                movies_list_bow = []
                i = 0
                for movie in rec_movies_bow:
                    movies_list_bow.append(MovieObj(movie.movie_id, movie.title, Fetch_poster(movie.movie_id)))
                    i = i + 1
                    if i >= 4:
                        break
                    if i >= len(rec_movies_bow):
                        break

                i = 0
                for movie in rec_movies:
                    movies_list.append(MovieObj(movie.movie_id, movie.title, Fetch_poster(movie.movie_id)))
                    i = i + 1
                    if i >= 4:
                        break
                    if i >= len(rec_movies):
                        break

            else:
                rec_movies_bow = []
                for id_bow in movie_recommendation_bow:
                    rec_movies_bow.append(Movie.objects.filter(movie_id=id_bow)[0])


                rec_movies = []
                for id in movie_recommendation:
                    temp = Movie.objects.filter(movie_id=id)[0]
                    if temp not in rec_movies_bow:
                        rec_movies.append(temp)

                movies_list_bow = []
                movies_list = []

                i = 0
                for movie in rec_movies_bow:
                    movies_list_bow.append(MovieObj(movie.movie_id, movie.title, Fetch_poster(movie.movie_id)))
                    i = i + 1
                    if i >= 4:
                        break
                    # if i >= len(rec_movies_bow):
                    #     break

                i = 0
                for movie in rec_movies:
                    movies_list.append(MovieObj(movie.movie_id, movie.title, Fetch_poster(movie.movie_id)))
                    i = i + 1
                    if i >= 4:
                        break
                    # if i >= len(rec_movies):
                    #     break

            return render(request, 'movieDetail.html', {
                'movie': movie_called,
                'poster': poster,
                'movies_data': movies_list,
                'movies_data_bow': movies_list_bow,
                'age_limit': age_limit
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../media/movies/video1.mp4")
@method_decorator(login_required, name='dispatch')
class ShowMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(movie_id=movie_id)

            movie = movie.videos.values()

            return render(request, 'showMovie.html', {
                'movie': list(movie),
                'path': path
            })
        except Movie.DoesNotExist:
            return redirect('core:profile_list')



def search_box(request):
    title1 = request.GET.get('title')
    if Debug:
        print(title1)
    payload = []
    movies_data = []
    if title1:
        title_objs = Movie.objects.filter(title__icontains = title1)
        for title_obj in title_objs:
            payload.append(title_obj.title)
            movies_data.append(title_obj.movie_id)

    return JsonResponse({'status': 200, 'payload': payload, 'movies_data': movies_data})



# class Searched_movie(View):
#     def searched_movie(self, request, title, *args, **kwargs):
#
#         return JsonResponse({'status': 200, 'payload': payload})