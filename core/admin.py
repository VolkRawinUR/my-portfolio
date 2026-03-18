from django.contrib import admin
from .models import UserProfile

# นำตาราง UserProfile ไปแสดงในระบบหลังบ้าน
admin.site.register(UserProfile)