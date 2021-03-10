from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from forms import ApplyForm

# Create your views here.
def register(request) :
  if request.method == 'POST' :
    form = UserRegisterForm(request.POST)
    if form.is_valid() :
      form.save()
      username = form.cleaned_data.get('username')
      return redirect('interviewselect')
  else :
    form = UserRegisterForm()
  return render(request, 'registration/register.html', {'form' : form})