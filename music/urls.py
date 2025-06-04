from django.urls import path,re_path

from music import views
app_name='music'

urlpatterns = [
 #/music/
 path('index/',views.IndexView.as_view(),name='index' ),

 path('register/', views.UserFormView.as_view(), name='register'),

 #/music/<albumid>/
 re_path (r'(?P<pk>[0-9]+)/',views.DetailView.as_view(), name='detail'),
 #/music/album/add/
 path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

 #/music/album/<albumid>/
 re_path (r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
 #/music/album/<albumid>/delete/
 path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

 path('', views.LoginView.as_view(), name='login'),
 
 path('logout/', views.LogoutView.as_view(), name='logout'),


]    
