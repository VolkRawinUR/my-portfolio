from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อ-นามสกุล")
    profile_picture = models.ImageField(upload_to='profile_pics/', verbose_name="รูปโปรไฟล์")
    shop_logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True, help_text="พิมพ์ประวัติหรือข้อมูลร้านตรงนี้ได้เลย")
    facebook_link = models.URLField(max_length=500, blank=True, null=True)
    instagram_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name