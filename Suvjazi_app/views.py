from django.shortcuts import render, get_object_or_404

from Suvjazi_app.models import Person, Institute

def index(request):
	institutes = Institute.objects.all()
	return render(request, 'Suvjazi_app/index.html', {'institutes': institutes, 'person': person})

def all_persons(request):
	persons = Person.objects.all()
	return render(request, 'Suvjazi_app/all_persons.html', {'persons': persons})

def person_detail(request, slug=None):
	person = get_object_or_404(Person, slug=slug)
	return render(request, 'Suvjazi_app/person_detail.html', {'person': person})

def institute_detail(request, slug=None):
	institute = get_object_or_404(Institute, slug=slug)
	return render(request, 'Suvjazi_app/institute_detail.html', {'institute': institute})
	