# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NonAdminAccountForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.

def index(request):
	login_form = LoginForm(prefix='logined')
	user_non_admin_form = NonAdminAccountForm(prefix='registered')
	if request.method == 'POST':
		if 'regbtn' in request.POST:
			print ("register yo")
			user_non_admin_form = NonAdminAccountForm(request.POST, prefix='registered')
			if user_non_admin_form.is_valid():
				user_non_admin_form.save()
				#email = request.POST['email']
				#username = User.objects.get(email=email.lower()).username
				#username = user_non_admin_form.cleaned_data.get('email')
				#raw_password = user_non_admin_form.cleaned_data.get('password1')
				#user = authenticate(request,username=username, password=raw_password)
				#login(request, user)
				return redirect('index')
		elif 'loginbtn' in request.POST:			
			login_form = LoginForm(request.POST, prefix='logined')
			username = request.POST['logined-email']
			password = request.POST['logined-password1']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print ("login yo")
			else:
				print("not login")
	else:
		user_non_admin_form = NonAdminAccountForm(prefix='registered')
		login_form = LoginForm( prefix='logined')
	context = {
		'login_form': login_form,
		'user_non_admin_form': user_non_admin_form,
	}
	return render(request, 'index.html', context)


def todo(request):
	pass