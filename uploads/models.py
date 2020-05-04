from django.db import models
from django.utils import timezone

class AddVid(models.Model):
    vid_type = models.CharField(max_length=220)

    def __str__(self):
        return self.vid_type

class Video(models.Model):
    vid_name = models.CharField(max_length=220)
    video_type = models.ForeignKey(AddVid, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(default=timezone.now)