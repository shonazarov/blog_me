from .views import BlogListView,BlogDetail
from django.urls import path


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    
]
