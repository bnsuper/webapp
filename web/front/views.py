from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def front_index(request):
	return render(request,'front_article_index.html')