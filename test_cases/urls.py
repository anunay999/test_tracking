from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('track/', views.track, name='track'),
    path('error/', views.error, name='error'),
    path('track/upload', views.upload, name='upload'),
    path('track/browse/', views.browse, name='browse'),
    path('browse/<str:module>/', views.module, name='module'),
    path('browse/edit/<str:module>', views.edit, name='edit'),
    path('logout/', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),


    
    
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]