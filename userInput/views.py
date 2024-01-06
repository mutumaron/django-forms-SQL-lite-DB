from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from .models import Review

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
        
        
class Success(TemplateView):
    template_name = "userInput/success.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]="This Works!"
        return context
    
    
class ReviewsListView(ListView):
    template_name = "userInput/review_list.html"
    model=Review
    context_object_name = "reviews"


class SingleReview(DetailView):
    template_name="userInput/single_review.html"
    model= Review
    
    
    
