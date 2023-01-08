from django.shortcuts import render


# Create your views here.

def registerGuide(request):
	return render(request, 'registerGuide.html')


def loginGuide(request):
	return render(request, 'loginGuide.html')