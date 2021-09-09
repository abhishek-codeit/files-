from .views import index
from django.urls.conf import path


urlpatterns = [
    path('', index, name="home"),

]
