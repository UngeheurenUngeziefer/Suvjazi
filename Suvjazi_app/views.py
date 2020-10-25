from django.shortcuts import render

def index(request):
	return render(request, 'Suvjazi_app/index.html')
