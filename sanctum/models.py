from django.db import models

class RepairTicket(models.Model):
    # ตัวเลือกสถานะงานซ่อม ให้ Admin กดเลือกได้ง่ายๆ
    STATUS_CHOICES = (
        ('PENDING', 'รอรับเครื่อง (Awaiting Arrival)'),
        ('INSPECTING', 'กำลังตรวจสอบ (Diagnosing Machine Spirit)'),
        ('WAITING_PARTS', 'รออะไหล่ (Awaiting Sacred Parts)'),
        ('REPAIRING', 'กำลังซ่อมแซม (Performing Rite of Repair)'),
        ('COMPLETED', 'ซ่อมเสร็จสิ้น (Sanctified & Ready)'),
        ('DELIVERED', 'ส่งมอบแล้ว (Returned to Owner)'),
    )

    customer_name = models.CharField(max_length=100, verbose_name="ชื่อลูกค้า")
    phone_number = models.CharField(max_length=20, verbose_name="เบอร์ติดต่อ")
    device_model = models.CharField(max_length=150, verbose_name="รุ่นอุปกรณ์ (Device)")
    issue_description = models.TextField(verbose_name="อาการเสีย (Corruption Details)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="สถานะงานซ่อม")
    
    # ระบบจะเก็บเวลาให้เองอัตโนมัติ
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่แจ้งซ่อม")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="อัปเดตสถานะล่าสุด")

    def __str__(self):
        # เวลาแสดงในหน้า Admin จะโชว์เป็น "Ticket #1 - ชื่อลูกค้า (รุ่นอุปกรณ์)"
        return f"Ticket #{self.id} - {self.customer_name} ({self.device_model})"