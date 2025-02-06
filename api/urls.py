from django.urls import path
from . import views



app_name = 'api'


urlpatterns = [
    path('list/',views.AppointmentList.as_view(),name='appointment_list_api'),
    path('list/<int:pk>/',views.AppointmentDetail.as_view(),name='appointment_detail_api'),
    path('booking/',views.UserFormAPIView.as_view(),name='booking_api'),
]