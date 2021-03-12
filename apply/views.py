from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth import update_session_auth_hash
from .models import Apply
from .forms import ApplyForm

