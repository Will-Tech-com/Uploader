from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Video


def index(request):
    videos = Video.objects.all()
    return render(request, 'uploads/index.html', { 'videos': videos })
    
def detail(request, upload_id):
    video = get_object_or_404(Video, id=upload_id)
    return render(request, 'uploads/detail.html', { 'video': video})
