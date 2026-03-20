from django.db import models

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

    def __str__(self):
        return self.name