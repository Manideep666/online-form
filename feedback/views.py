from django.shortcuts import render
from feedback.forms import feedbackform
from feedback.models import feedbackmodel
# Create your views here.
def createfeed(request):
    form=feedbackform()
    return render(request,"home.html",{"form":form})