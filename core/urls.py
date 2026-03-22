from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # --- เส้นทางใหม่สำหรับหน้าข่าวสาร ---
    path('news/', views.news_page, name='news_page'), 
]