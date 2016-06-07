from django.shortcuts import render
from band.models import Video, Album
import datetime

def index(request):
	now = datetime.datetime.now()
	data = Video.objects.get(main = True)
	
	return render(request, 'band/home.html', {"video": data, "year": now.year})

def merch(request):
	now = datetime.datetime.now()
	data = Album.objects.all()

	return render(request, 'band/merch.html', { "album": data, "year": now.year})