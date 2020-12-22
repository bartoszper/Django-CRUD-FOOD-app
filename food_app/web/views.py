from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    return render(request, 'index.html',{'item_list':item_list})

def item(request):
    return HttpResponse('This is item view')

