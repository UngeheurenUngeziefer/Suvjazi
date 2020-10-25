from django.shortcuts import render

from Suvjazi_app.models import Institute

def index(request):
	institutes = Institute.objects.all()
	return render(request, 'Suvjazi_app/index.html', {'institutes': institutes})
