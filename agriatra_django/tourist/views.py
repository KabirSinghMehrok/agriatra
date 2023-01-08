from django.shortcuts import render

# Create your views here.


def registerTourist(request):
	return render(request, 'registerTourist.html')


def loginTourist(request):
	return render(request, 'loginTourist.html')


def viewNFT(request):
	return render(request, 'nft.html')


def beeKeeping(request):
	return render(request, 'beeKeeping.html')


def chandigarhFarms(request):
	return render(request, 'chandigarhFarms.html')


def chandigarhFarmsVisited(request):
	return render(request, 'chandigarhFarmsVisited.html')
