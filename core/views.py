from django.shortcuts import render
from .models import UserProfile

def home(request):
    # ดึงข้อมูลโปรไฟล์อันแรกจากฐานข้อมูลมาใช้งาน
    profile = UserProfile.objects.first()
    return render(request, 'index.html', {'profile': profile})