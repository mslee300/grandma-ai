from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'grandmaai/grandma_ai.html')

def signup_redirect(request):
    messages.error(request, 'Something wrong here, it may be that you already have account!')
    return redirect('/grandmaai')