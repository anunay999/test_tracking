from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('track/', views.track, name='track')
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]