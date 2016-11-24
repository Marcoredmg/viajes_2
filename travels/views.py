from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Travel
from django.template import loader
from .forms import TravelForm


def hello_world(request):
	travel = Travel.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'travel': travel
	}
	return HttpResponse(template.render(context, request))

def travel_detail(request, pk):
	travel = get_object_or_404(Travel, pk=pk)
	template = loader.get_template('travel_detail.html')
	context = {
		'travel': travel
	}
	return HttpResponse(template.render(context, request))


def new_travel(request):
	if request.method == 'POST':
		form = TravelForm(request.POST, request.FILES)
		if form.is_valid():
			travel = form.save()
			travel.save()
			return HttpResponseRedirect('/')
	else:
		form = TravelForm()

	template = loader.get_template('new_travel.html')
	context = {
		'form': form
	}
	return HttpResponse(template.render(context, request))	