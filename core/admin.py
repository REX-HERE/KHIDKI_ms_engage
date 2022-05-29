from django.contrib import admin
from .models import CustomUser, Profile, Movie, Video, Dropdown
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class Movie_resources(resources.ModelResource):

    class Meta:
        model = Movie
        fields = ('id', 'movie_id', 'title', 'description')

class Movie_admin(ImportExportModelAdmin):
    resource_class = Movie_resources


class Dropdown_resources(resources.ModelResource):

    class Meta:
        model = Dropdown
        fields = ('id','title')

class Dropdown_admin(ImportExportModelAdmin):
    resource_class = Dropdown_resources


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie, Movie_admin)
admin.site.register(Video)


admin.site.register(Dropdown, Dropdown_admin)