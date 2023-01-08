from django.shortcuts import render

# Create your views here.


def registerHost(request):
	return render(request, 'registerHost.html')

def loginHost(request):
	return render(request, 'loginHost.html')

def viewFarmList(request):
	return render(request, 'farmlist.html')


def manageAccommodations(request):
	return render(request, 'manage.html')


def viewProfile(request):
	return render(request, 'farmer.html')
