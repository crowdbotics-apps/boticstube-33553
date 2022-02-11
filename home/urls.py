from django.urls import path
from home import views

urlpatterns = [
    path('admin/', views.yousuck, name='yousuck'),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),

 # Hall
    path('vidz/create', views.CreateHall.as_view(), name='create_hall'),
    path('vidz/<int:pk>', views.DetailHall.as_view(), name='detail_hall'),
    path('vidz/<int:pk>/update', views.UpdateHall.as_view(), name='update_hall'),
    path('vidz/<int:pk>/delete', views.DeleteHall.as_view(), name='delete_hall'),

    #Video
    path('vidz/<int:pk>/addvideo', views.add_video, name='add_video'),
    path('vidz/search', views.video_search, name='video_search'),
    path('vidz/<int:pk>/delete', views.DeleteVideo.as_view(), name='delete_video'),
]