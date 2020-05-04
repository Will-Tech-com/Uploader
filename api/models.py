from django.db import models
from tastypie.resources import ModelResource
from uploads.models import Video

class VideoResource(ModelResource):
    class Meta:
        queryset = Video.objects.all()
        resource_name = 'uploads'
    