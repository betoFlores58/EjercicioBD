from django.urls import path
from .views import HomePageView,OtraPageView

urlpatterns=[
    path('', HomePageView.as_view(),name='home'),
    path('otra', OtraPageView.as_view(),name='otra'),
]