from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from grandmaai.models import Phone
from grandmaai.forms import PhoneForm
from grandmaai.models import Goal, Phone, Level
import openai
from twilio.rest import Client

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


def send_message(dest_num, message_content):
  account_sid = ''
  auth_token = ''
  client = Client(account_sid, auth_token)
  
  message = client.messages.create(
    from_='',
    body=message_content,
    to=f'+1{dest_num}'
  )
  
  print(message.sid)
  print(f"Sent message to {dest_num}")
  
  
import schedule
import time

def schedule_messages():
  phones = Phone.objects.all()
  for phone in phones:
    user_goal = str(Goal.objects.filter(author=phone.author).last())
    print(f'user goal: {user_goal}')
    level = str(Level.objects.filter(author=phone.author).last())
    print(f'user level: {level}')
    generated_message = '👵🏻 Grandma AI says: ' + generate_message(user_goal, level)
    print(f'generated message: {generated_message}')
    dest_num = str(phone).replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    print(f'sending to: {dest_num}')
    send_message(dest_num, generated_message)

    # Schedule messages based on user's preferred difficulty level
    schedule.every(12).hours.do(schedule_messages).tag('hard')
    schedule.every(24).hours.do(schedule_messages).tag('medium')
    schedule.every(48).hours.do(schedule_messages).tag('easy')
    
    while True:
      schedule.run_pending()
      time.sleep
  
  
@login_required(login_url='common:login')
def phone_create(request):
  if request.method == 'POST':
      form = PhoneForm(request.POST)
      if form.is_valid():
          phone = form.save(commit=False)
          phone.author = request.user  # author 속성에 로그인 계정 저장
          phone.save()
          # generate AI message
          user_goal = str(Goal.objects.filter(author=request.user).last())
          print(f'user goal: {user_goal}')
          generated_message = '👵🏻 Grandma AI says: ' + generate_message(request, user_goal)
          print(f'generated message: {generated_message}')
          # Send message
          dest_num = str(Phone.objects.filter(author=request.user).last()).replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
          print(f'sending to: {dest_num}')
          send_message(dest_num, generated_message)
          
          return redirect('/grandmaai/subscribed')
  else:
      form = PhoneForm()
  context = {'form': form}
  return render(request, 'grandmaai/phone_create.html', context)


@login_required(login_url='common:login')
def phone_modify(request, phone_id):
  return render(request, 'grandmaai/phone_create.html')
