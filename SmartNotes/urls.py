
from django.contrib import admin
from django.urls import path, include
from App1 import views
import App1



urlpatterns = [
    path("admin/", admin.site.urls),
    path('home', views.home),
    path('currentTime', views.currentTime),
    # path('', views.default),
    # path('', include(App1.urls))
]
