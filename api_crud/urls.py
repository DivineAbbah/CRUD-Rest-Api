from django.urls import path

from . import views


urlpatterns = [

  path('', views.index, name='index'),

  path('api/v1/movies/', include('movies.urls')),

  path('api/v1/auth/', include('authentication.urls')),

  path('admin/', admin.site.urls),

]
