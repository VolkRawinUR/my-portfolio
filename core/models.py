from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อ-นามสกุล")
    profile_picture = models.ImageField(upload_to='profile_pics/', verbose_name="รูปโปรไฟล์")
    bio = models.TextField(verbose_name="ประวัติส่วนตัว")
    facebook_link = models.URLField(max_length=200, blank=True, verbose_name="Facebook URL")
    instagram_link = models.URLField(max_length=200, blank=True, verbose_name="Instagram URL")

    def __str__(self):
        return self.name