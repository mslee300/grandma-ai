from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from grandmaai.models import Goal
from grandmaai.forms import GoalForm


@login_required(login_url='common:signup')
def goal_create(request):
  if request.method == 'POST':
      form = GoalForm(request.POST)
      if form.is_valid():
          goal = form.save(commit=False)
          goal.author = request.user  # author 속성에 로그인 계정 저장
          goal.save()
          return redirect('/grandmaai/level/create')
  else:
      form = GoalForm()
  context = {'form': form}
  return render(request, 'grandmaai/goal_create.html', context)
  

@login_required(login_url='common:login')
def goal_modify(request, goal_id):
  return render(request, 'grandmaai/goal_create.html')