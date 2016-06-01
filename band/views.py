from django.shortcuts import render
from band.models import Video
import datetime

def index(request):
	now = datetime.datetime.now()
	data = Video.objects.get(main = True)
	
	return render(request, 'band/home.html', {"video": data, "year": now.year})