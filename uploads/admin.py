from django.contrib import admin
from .models import AddVid, Video

class AddVidAdmin(admin.ModelAdmin):
    list_display = ('id', 'vid_type')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('vid_name', 'video_type', 'date_uploaded')

admin.site.register(AddVid, AddVidAdmin) 
admin.site.register(Video, VideoAdmin)
