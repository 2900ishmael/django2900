from django.contrib import admin
from django.urls import path,include
from homixidegang import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info),
    path('table/', views.table),
    path('collection/', views.collection),
]