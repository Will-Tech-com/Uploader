from django.urls import path
from . import views

app_name = 'uploads'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:upload_id>', views.detail, name='detail')
]
