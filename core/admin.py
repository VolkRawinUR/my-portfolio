from django.contrib import admin
from .models import UserProfile, News  # <-- เพิ่มคำว่า News เข้ามาตรงบรรทัดนี้ครับ

# นำตาราง UserProfile ไปแสดงในระบบหลังบ้าน
admin.site.register(UserProfile)

# ==========================================
# ส่วนที่เพิ่มใหม่: จัดการกระดานข่าวสาร (News)
# ==========================================
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    # แสดงคอลัมน์ในหน้า Admin
    list_display = ('title', 'is_published', 'created_at')
    
    # เพิ่มตัวกรองข่าวด้านขวามือ (เช่น ดูเฉพาะข่าวที่เผยแพร่แล้ว)
    list_filter = ('is_published', 'created_at')
    
    # เพิ่มช่องค้นหาหัวข้อข่าว
    search_fields = ('title', 'content')