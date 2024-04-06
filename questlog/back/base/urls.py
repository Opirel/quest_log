"""
base
"""
from django.contrib import admin
from django.urls import path
from base import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('players', views.Pc),
    path('players/<int:id>', views.Pc),
    path('quests/<int:id>', views.quests),
    path('quests', views.quests),

]
