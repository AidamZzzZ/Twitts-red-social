from django.urls import path
from .views import dashboard, profile_list, detail_profile

app_name = "twitts"
urlpatterns = [
    path('', dashboard, name="home"),
    path('list/', profile_list, name="list"),
    path('profile/<int:pk>', detail_profile, name="profile"),
]
