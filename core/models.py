from django.db import models
from django.utils import timezone

class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อ-นามสกุล")
    profile_picture = models.ImageField(upload_to='profile_pics/', verbose_name="รูปโปรไฟล์")
    shop_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True, help_text="พิมพ์ประวัติหรือข้อมูลร้านตรงนี้ได้เลย")
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)
    service_history = models.TextField(blank=True, null=True, verbose_name="ประวัติการรับใช้ (Service History)")
    knowledge_archives = models.TextField(blank=True, null=True, verbose_name="คลังความรู้ (Knowledge Archives)")
    site_title = models.CharField(max_length=200, default="Tech-Priest: รวินท์ งามเลิศ (Volk)", verbose_name="หัวข้อหน้าเว็บ")
    faction = models.CharField(max_length=100, default="Volkgaard Tech", verbose_name="สังกัด (Faction)")
    role = models.CharField(max_length=100, default="IT Support Technician", verbose_name="บทบาท (Role)")
    location = models.CharField(max_length=100, default="Terra (Earth)", verbose_name="สถานที่ตั้ง")
    
    
class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="หัวข้อข่าว")
    content = models.TextField(verbose_name="เนื้อหาข่าว")
    
    # --- 2 บรรทัดนี้คือของใหม่ที่เพิ่มเข้ามาครับ ---
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="รูปภาพประกอบ (ถ้ามี)")
    video_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="ลิงก์วิดีโอ (เช่น YouTube)", help_text="ก๊อปปี้ลิงก์ YouTube มาวางได้เลยครับ")
    # ----------------------------------------
    
    is_published = models.BooleanField(default=True, verbose_name="สถานะเผยแพร่ (ขึ้นเว็บ)")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่ประกาศ")

    class Meta:
        verbose_name = "ประกาศข่าวสาร"
        verbose_name_plural = "กระดานข่าวสาร (News)"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
