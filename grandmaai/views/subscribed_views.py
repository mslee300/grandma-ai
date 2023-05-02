from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

@login_required(login_url='common:login')
def subscribed(request):
  return render(request, 'grandmaai/subscribed.html')