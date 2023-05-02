from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

@login_required(login_url='common:login')
def channel_create(request):
  return render(request, 'grandmaai/channel_create.html')

@login_required(login_url='common:login')
def channel_modify(request, channel_id):
  return render(request, 'grandmaai/channel_create.html')