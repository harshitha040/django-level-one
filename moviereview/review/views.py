from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def basic(request):
    return HttpResponse("hell0 world")

def movie_info(request):
    movie=request.GET.get('movie')
    date=request.GET.get('date')
    return JsonResponse({'status':"success",'result':{'movie_name':movie,'release_date':date}},status=200)