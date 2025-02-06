from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# csrf_exempt
# from .models import Appointment
# from django.core.mail import send_mail
# import json

# @csrf_exempt
# def book_appointment(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#
#         name = data.get('name')  # نام کاربر
#         phone_number = data.get('phone_number')  # شماره تلفن
#         email = data.get('email')
#         date = data.get('date')
#         time = data.get('time')
#
#         try:
#             appointment = Appointment(
#                 name=name,
#                 phone_number=phone_number,
#                 email=email,
#                 date=date,
#                 time=time,
#             )
#             appointment.save()
#
#             # ارسال ایمیل
#             send_mail(
#                 'نوبت شما ثبت شد',
#                 f'سلام {name}، نوبت شما برای تاریخ {date} و ساعت {time} ثبت شد.',
#                 'khashayar.shirazi.71@gmail.com',
#                 [email],
#             )
#
#             return JsonResponse({'message': 'نوبت شما با موفقیت ثبت شد!'}, status=201)
#
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
#
#
#     return JsonResponse({'error': 'فقط درخواست POST مجاز است.'}, status=405)

# def create_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AppointmentForm()
#
#     return render(request,'appoints.html',{'form':form})
