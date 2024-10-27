from django.shortcuts import redirect, render
from django.http import HttpResponsePermanentRedirect

def home(request):
    return render(request,"index.html")