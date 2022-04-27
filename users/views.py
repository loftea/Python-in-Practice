import imp
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(r):
    if r.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=r.POST)

        if form.is_valid():
            new_user = form.save()
            login(r, new_user)
            return redirect('learning_logs:index')
