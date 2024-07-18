from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import get_user_model

from apps.users.forms import UserForm

User = get_user_model()

