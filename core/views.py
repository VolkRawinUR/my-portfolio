from django.shortcuts import render
from .models import UserProfile, News  # <--- อย่าลืมเพิ่ม News ตรงนี้นะครับ

def home(request): # (ชื่อฟังก์ชันของคุณอาจจะเป็น home หรือ index)
    profile = UserProfile.objects.first()
    
    # สั่งให้ดึงข่าวสารที่ตั้งค่า "เผยแพร่ (is_published=True)" มาโชว์ (เอาแค่ 5 ข่าวล่าสุด)
    news_list = News.objects.filter(is_published=True).order_by('-created_at')[:5]
    
    # หิ้ว news_list ใส่กระเป๋า (context) ส่งไปให้หน้าเว็บด้วย
    context = {
        'profile': profile,
        'news_list': news_list,  # <--- เพิ่มบรรทัดนี้
    }
    return render(request, 'index.html', context) # (ชื่อไฟล์อาจจะเป็น core/index.html)

def news_page(request):
    # ดึงข่าวทั้งหมดที่ตั้งว่าเผยแพร่ เรียงจากใหม่ไปเก่า
    news_list = News.objects.filter(is_published=True).order_by('-created_at')
    
    context = {
        'news_list': news_list,
    }
    # สั่งให้ไปเปิดหน้า news.html 
    return render(request, 'news.html', context)