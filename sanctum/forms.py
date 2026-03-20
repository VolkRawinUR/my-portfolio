from django import forms
from .models import RepairTicket

class RepairTicketForm(forms.ModelForm):
    class Meta:
        model = RepairTicket
        # เลือกฟิลด์ที่จะให้ลูกค้ากรอก (สังเกตว่าเราไม่ให้ลูกค้าเลือก "สถานะ" เอง)
        fields = ['customer_name', 'phone_number', 'device_model', 'issue_description']
        
        # ตกแต่งกล่องข้อความให้รองรับ CSS ของหน้าเว็บ
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อ-นามสกุล'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เบอร์โทรศัพท์ติดต่อ'}),
            'device_model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น Notebook ASUS, PC ประกอบ'}),
            'issue_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'อธิบายอาการเสียให้ละเอียดที่สุดเท่าที่ทำได้'}),
        }