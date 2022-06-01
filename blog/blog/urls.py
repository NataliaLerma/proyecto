#blog/urls.py
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #libreria para imagenes
from .views import BlogListView,BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView

urlpatterns=[
	path('post/new/', BlogCreateView.as_view(), name='post_new'), #new
	path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),#new
	path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name='post_delete'),
	path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name='post_edit'),
	path('', BlogListView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()#para las imagenes

