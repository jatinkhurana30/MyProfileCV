from django.http import HttpResponse
from django.shortcuts import render
from .models import People_Comments
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(value)
# Create your views here.

def home(request):

    people_comments = People_Comments.objects.all()

    return render(request,'index.html',{'people_comments':people_comments})