from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

class Appointment(models.Model):
    name = models.CharField(max_length=100)  # نام کاربر
    phone_number = models.CharField(max_length=15)  # شماره تلفن کاربر
    email = models.EmailField()  # ایمیل کاربر
    date = models.DateField()  # تاریخ نوبت
    time = models.TimeField()  # ساعت نوبت

    def clean(self):
        # 1. نوبت برای روز جمعه نده
        if self.date.weekday() == 5:  # جمعه
            raise ValidationError("نوبت‌گیری برای روز جمعه ممکن نیست.")

        # 2. بررسی ساعات مجاز
        allowed_hours = {
            5: [10, 11, 12],  # پنجشنبه
            0: [10, 11, 12, 16, 17, 18, 19, 20],  # شنبه تا چهارشنبه
            1: [10, 11, 12, 16, 17, 18, 19, 20],
            2: [10, 11, 12, 16, 17, 18, 19, 20],
            3: [10, 11, 12, 16, 17, 18, 19, 20],
            4: [10, 11, 12, 16, 17, 18, 19, 20],
        }

        if self.date.weekday() not in allowed_hours or self.time.hour not in allowed_hours[self.date.weekday()]:
            raise ValidationError("ساعت انتخابی در روز موردنظر مجاز نیست.")

        # 3. بررسی تکراری نبودن تاریخ و ساعت
        if Appointment.objects.filter(date=self.date, time=self.time).exists():
            raise ValidationError("این تاریخ و ساعت قبلاً انتخاب شده است.")

        # 4. جلوگیری از انتخاب روزها و ساعات گذشته
        if self.date < datetime.today().date() or (
            self.date == datetime.today().date() and self.time < datetime.now().time()
        ):
            raise ValidationError("نمی‌توانید روزها و ساعات گذشته را انتخاب کنید.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


