from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from grandmaai.models import Level
from grandmaai.forms import LevelForm

@login_required(login_url='common:login')
def level_create(request):
  if request.method == 'POST':
      form = LevelForm(request.POST)
      if form.is_valid():
          level = form.save(commit=False)
          level.author = request.user  # author 속성에 로그인 계정 저장
          level.save()
          return redirect('/grandmaai/channel/create')
  else:
      form = LevelForm()
  context = {'form': form}
  return render(request, 'grandmaai/level_create.html', context)


@login_required(login_url='common:login')
def level_modify(request, level_id):
  return render(request, 'grandmaai/level_create.html')