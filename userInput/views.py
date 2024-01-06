from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        
        return render(request,"userInput/userInput.html",{
            "form":form
        })
         
         
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/success")
        
        return render(request,"userInput/userInput.html",{
            "form":form
         })
        

def success (request):
    return render(request,"userInput/success.html")