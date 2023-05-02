from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from grandmaai.models import Email
from grandmaai.forms import EmailForm
from grandmaai.models import Goal, Email, Level
import openai
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

openai.api_key = ""

def generate_message(request, prompt):
  replaced_prompt = prompt.replace('I want to ', '').replace('.', '')
  print(f'replaced prompt: {replaced_prompt}')
  if str(Level.objects.filter(author=request.user).last()) == 'h':
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      temperature=1,
      max_tokens=120,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      messages=[
            {"role": "user", "content": f"Give a nagging message for someone who wants to {replaced_prompt}"}
        ]
    )
  else:
      response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      temperature=1,
      max_tokens=120,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      messages=[
            {"role": "user", "content": f"Give a motivational message for someone who wants to {replaced_prompt}"}
        ]
    )
  return response['choices'][0]['message']['content']


def send_email(request, to_email, message):
    mail_subject = '👵🏻 Grandma AI sent you a message!'
    message = render_to_string('template_message.html', {
        'message': message,
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
      pass
    else:
        messages.error(request, f'Problem sending email to {to_email}, please check if you typed it correctly.')
        
        
import schedule
import time

def schedule_messages():
  emails = Email.objects.all()
  for email in emails:
    user_goal = str(Goal.objects.filter(author=email.author).last())
    print(f'user goal: {user_goal}')
    level = str(Level.objects.filter(author=email.author).last())
    print(f'user level: {level}')
    generated_message = '👵🏻 Grandma AI says: ' + generate_message(user_goal, level)
    print(f'generated message: {generated_message}')
    dest_num = str(email).replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    print(f'sending to: {dest_num}')
    send_email(dest_num, generated_message)

    # Schedule messages based on user's preferred difficulty level
    schedule.every(12).hours.do(schedule_messages).tag('hard')
    schedule.every(24).hours.do(schedule_messages).tag('medium')
    schedule.every(48).hours.do(schedule_messages).tag('easy')
    
    while True:
      schedule.run_pending()
      time.sleep
      

@login_required(login_url='common:login')
def email_create(request):
  if request.method == 'POST':
      form = EmailForm(request.POST)
      if form.is_valid():
          email = form.save(commit=False)
          email.author = request.user  # author 속성에 로그인 계정 저장
          email.save()
          # generate AI message
          user_goal = str(Goal.objects.filter(author=request.user).last())
          print(f'user goal: {user_goal}')
          generated_message = generate_message(request, user_goal)
          print(f'generated message: {generated_message}')
          # send generated message to email
          user_email = str(Email.objects.filter(author=request.user).last())
          print(f'user email: {user_email}')
          send_email(request, user_email, generated_message)
          return redirect('/grandmaai/subscribed')
  else:
      form = EmailForm()
  context = {'form': form}
  return render(request, 'grandmaai/email_create.html', context)



@login_required(login_url='common:login')
def email_modify(request, email_id):
  return render(request, 'grandmaai/email_create.html')
