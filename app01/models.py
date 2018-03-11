from django.db import models
from MROS import settings


class Meeting_room(models.Model):
    title = models.CharField(verbose_name="会议室名",max_length=32)

    def __str__(self):
        return  self.title


class User(models.Model):
    name = models.CharField(verbose_name="用户名",max_length=32)
    pwd = models.CharField(verbose_name="密码",max_length=32)
    def __str__(self):
        return  self.name


class Booking(models.Model):
    date = models.DateField(verbose_name="日期")
    times = models.IntegerField(verbose_name="时间段",choices=settings.times_list)
    meeting_room=models.ForeignKey(verbose_name="会议室",to=Meeting_room)
    user=models.ForeignKey(to=User,verbose_name="预定人")

    class Meta:
        unique_together=[('date','times','meeting_room')]
# Create your models here.
