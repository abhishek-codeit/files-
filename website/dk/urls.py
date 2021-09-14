from .views import index, cont
from django.urls.conf import path


urlpatterns = [
    path('', index, name="home"),
    path('events', index, name="events"),
    path('contact', cont, name="contact"),
    path('about', cont, name="about"),
    


]
