from django.urls import path
from .views import SlackdeetViews


urlpatterns = [
    path('slackdeet', SlackdeetViews.as_view(), name='deetview')
]