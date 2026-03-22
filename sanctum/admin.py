from django.contrib import admin
from .models import RepairTicket

@admin.register(RepairTicket)
class RepairTicketAdmin(admin.ModelAdmin):
    # 1. คอลัมน์ที่จะแสดงในตารางหน้าแรก (เรียงตามลำดับ)
    list_display = ('id', 'customer_name', 'phone_number', 'device_model', 'status', 'created_at')
    
    # 2. เพิ่มกล่อง "ตัวกรอง (Filter)" ด้านขวามือ ให้กดดูเฉพาะงานที่ 'รอรับเครื่อง' หรือ 'ซ่อมเสร็จ' ได้เลย
    list_filter = ('status', 'created_at')
    
    # 3. เพิ่ม "ช่องค้นหา (Search Bar)" ด้านบนสุด (ค้นจากชื่อ, เบอร์โทร, หรือรุ่นอุปกรณ์ก็ได้)
    search_fields = ('customer_name', 'phone_number', 'device_model')
    
    # 4. จัดหมวดหมู่ข้อมูลเวลาคลิกเข้าไปแก้ไขตั๋วแต่ละใบ ให้ดูเป็นระเบียบ
    fieldsets = (
        ('ข้อมูลผู้ร้องขอ (Client Data)', {
            'fields': ('customer_name', 'phone_number')
        }),
        ('ข้อมูลวิญญาณเครื่องจักร (Machine Spirit Data)', {
            'fields': ('device_model', 'issue_description')
        }),
        ('สถานะพิธีกรรม (Rite Status)', {
            'fields': ('status',)
        }),
    )