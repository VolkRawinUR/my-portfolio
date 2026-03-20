from django.shortcuts import render, redirect
from .forms import RepairTicketForm
from .models import RepairTicket

def create_ticket(request):
    if request.method == 'POST':
        form = RepairTicketForm(request.POST)
        if form.is_valid():
            form.save() # บันทึกข้อมูลลงตาราง
            return redirect('ticket_success') # บันทึกเสร็จแล้วเด้งไปหน้าสำเร็จ
    else:
        form = RepairTicketForm()

    return render(request, 'sanctum/create_ticket.html', {'form': form})

def ticket_success(request):
    return render(request, 'sanctum/success.html')
def track_ticket(request):
    # ดึงคำค้นหา (เบอร์โทร หรือ ชื่อ) ที่ลูกค้าพิมพ์เข้ามา
    query = request.GET.get('q')
    tickets = None
    
    if query:
        # สั่งให้ค้นหาในตารางฐานข้อมูล ว่ามีเบอร์โทร หรือ ชื่อ ตรงกับที่พิมพ์มาไหม
        tickets = RepairTicket.objects.filter(phone_number__icontains=query) | RepairTicket.objects.filter(customer_name__icontains=query)
        # เรียงลำดับให้อันล่าสุดขึ้นก่อน
        tickets = tickets.order_by('-created_at')

    return render(request, 'sanctum/track_ticket.html', {'tickets': tickets, 'query': query})