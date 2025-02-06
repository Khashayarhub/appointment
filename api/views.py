from .models import Appointments
from .serilizers import AppointmentSerializer,UserSerializer
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from django.core.mail import send_mail
from kavenegar import *

# Create your views here.
class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer

class UserFormAPIView(generics.CreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Save the instance
        instance = serializer.save()

        # Prepare email details
        subject = "Appointment Confirmation"
        message = f"Hello {instance.last_name},\n\nYour appointment has been successfully booked. Details are as follows:\nDate: {instance.date}\nTime: {instance.time}\n\nThank you!"
        recipient_email = instance.email  # Ensure your Appointment model has an 'email' field

        # Send the email
        send_mail(
            subject,
            message,
            'khashayar.shirazi.71@gmail.com',  # Replace with your email address
            [recipient_email],
            fail_silently=False,
        )

        # Prepare and send SMS using Kavenegar API
        try:
            api = KavenegarAPI('7A2F305A446737304F382B3567452F553471434D683673746B6D744732307345666953486E4A6D447936493D')
            params = {
                'receptor': instance.phone,  # Ensure your Appointment model has a 'phone_number' field
                'template': 'test-token',
                'token': instance.first_name,
                'token2': str(instance.date),
                'token3': str(instance.time),
                'type': 'sms',  # sms vs call
            }
            response = api.verify_lookup(params)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)