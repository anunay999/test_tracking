from django.urls import path
from . import views
from .views import ChartData,DashboardView,EditModelView

app_name = 'myapp'
urlpatterns = [
    #path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('track/', views.track, name='track'),
    path('error/', views.error, name='error'),
    path('track/upload', views.upload, name='upload'),
    path('track/browse/', views.browse, name='browse'),
    path('browse/<str:module>/', views.module, name='module'),
    path('browse/<str:module>/<str:category>', views.category, name='category'),
    path('edit/<str:module>', views.edit, name='edit'),
    #path('browse/edit/<str:module>', EditModelView.as_view() , name='edit'),
    path('browse/edit/<str:module>/<str:category>', views.edit_category, name='edit_category'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/data', ChartData.as_view(),name='dashboard_data'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


    
    
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]