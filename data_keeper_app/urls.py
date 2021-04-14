from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_page, name='welcome-page'),
    path('log-in', views.user_details_view, name='log-in'),
    path('home-page', views.home_page, name='home-page'),
    path('test', views.input_click_evnt, name='test'),

]