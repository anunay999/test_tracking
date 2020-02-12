from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('track/', views.track, name='track'),
    path('error/', views.error, name='error'),
    path('browse/', views.browse, name='browse'),
    path('module/', views.module, name='module')
    
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]