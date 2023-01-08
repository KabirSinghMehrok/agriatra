from django.shortcuts import render


# Create your views here.

def index(request):
	return render(request, 'landing.html')


def aboutPage(request):
	return render(request, 'aboutPage.html')