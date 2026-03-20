from django.urls import path
from . import views

urlpatterns = [
    # ลิงก์สำหรับหน้าฟอร์มแจ้งซ่อม
    path('repair/', views.create_ticket, name='create_ticket'),
    # ลิงก์สำหรับหน้าแจ้งเตือนเมื่อบันทึกสำเร็จ
    path('track/', views.track_ticket, name='track_ticket'),
    path('repair/success/', views.ticket_success, name='ticket_success'),
]