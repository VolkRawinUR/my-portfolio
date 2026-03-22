from django.urls import path
from . import views

urlpatterns = [
    # ถนนสายที่ 1: หน้าสร้างตั๋วแจ้งซ่อม
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    
    # ถนนสายที่ 2: หน้ารับเรื่องสำเร็จ (พร้อมโชว์เลขตั๋ว)
    path('success/<int:ticket_id>/', views.ticket_success, name='ticket_success'),
    
    # ถนนสายที่ 3: หน้าติดตามสถานะ
    path('track-ticket/', views.track_ticket, name='track_ticket'),
]