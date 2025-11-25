from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from review.models import Movie_details
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def basic(request):
    return HttpResponse("hell0 world")

def movie_info(request):
    movie=request.GET.get('movie')
    date=request.GET.get('date')
    return JsonResponse({'status':"success",'result':{'movie_name':movie,'release_date':date}},status=200)


@csrf_exempt
def movies(request):
    if request.method=='POST':
        data=json.loads(request.body)
        movie=Movie_details.objects.create(movie_name=data.get("movie_name"),release_date=data.get("release_date"),budget=data.get("budget"),rating=data.get("rating"))
        return JsonResponse({'status':"success",'message':"Movie record inserted successfully","data":data},status=200)
    return JsonResponse({'error':"error occured"},status=400)



